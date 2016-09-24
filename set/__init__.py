# -*- coding: utf-8 -*-

"""
Based on a stripped-down version of the AWS Signature v4 implementation.

Copyright (c) 2015-2016 [WePay](https://wepay.com).

<http://opensource.org/licenses/Apache2.0>
"""

from __future__ import print_function
import hashlib
import hmac
import six


class Signer(object):
    """
    The Signer class is designed for those who are signing data on behalf of a public-private keypair.

    In principle, the "client party" has public key (i.e., `client_id`) has a matching private key
    (i.e., `client_secret`) that can be verified by both the signer, as well as the client, but
    by nobody else as we don't want to make forgeries possible.

    The "signing party" has a simple an identifier which acts as an additional piece of entropy in the
    algorithm, and can help differentiate between multiple signing parties if the client party does
    something like try to use the same public-private keypair independently of a signing party
    (as is common with GPG signing).

    For example, in the original AWS implementation, the "self key" for AWS was "AWS4".

    **Compatibility:**

    Tested against the following Python versions:

    * Python 2.7
    * Python 3.3
    * Python 3.4
    * Python 3.5
    * Python 3.6 (dev)
    * Pypy (~2.7.10)
    * Pypy3 (~3.2.5)

    **Import:**

        from wepay.signer import Signer

    """

    def __init__(self, client_id, client_secret, self_key="WePay", hash_algo=None):
        """
        Constructs a new instance of this class.

        `client_id (string)`: A string which is the public portion of the keypair identifying the client party. The
            pairing of the public and private portions of the keypair should only be known to the client party and the
            signing party.

        `client_secret (string)`: A string which is the private portion of the keypair identifying the client party.
            The pairing of the public and private portions of the keypair should only be known to the client party and
            the signing party.

        `self_key (string)`: A string which identifies the signing party and adds additional entropy. The default value
            is `WePay`.

        `hash_algo (object)`: The hash algorithm to use for signing. The default value is `hashlib.sha512`. Allowed
            values are any `hashlib.*` method name that is listed in `hashlib.algorithms_available`.
        """

        if hash_algo is None:
            hash_algo = hashlib.sha512

        self.client_id = "{client_id}".format(client_id=client_id)
        """Returns the value of attribute client_id."""

        self.client_secret = "{client_secret}".format(client_secret=client_secret)
        """Returns the value of attribute client_secret."""

        self.self_key = "{self_key}".format(self_key=self_key)
        """Returns the value of attribute self_key. The default value is `WePay`."""

        self.hash_algo = hash_algo
        """Returns the value of attribute hash_algo. The default value is `hashlib.sha512`."""

    def sign(self, **kwargs):
        """
        Sign the payload to produce a signature for its contents.

        `token (string)`: The one-time-use token. **Required**.

        `page (string)`: The WePay URL to access. **Required**.

        `redirect_uri (string)`: The partner URL to return to once the action is completed. **Required**.

        `return (string)`: The signature for the payload contents.
        """

        merged_payload = {}

        if kwargs is not None:
            for key, value in six.iteritems(kwargs):
                merged_payload[key] = value

        merged_payload['client_id'] = self.client_id
        merged_payload['client_secret'] = self.client_secret

        scope = self.__create_scope()
        context = self.__create_context(**merged_payload)
        s2s = self.__create_string_to_sign(scope, context)
        signing_key = self.__get_signing_salt()

        signature = hmac.new(
            signing_key,
            six.u(s2s).encode('utf-8'),
            self.hash_algo
        ).hexdigest()

        return signature

    def generate_query_string_params(self, **kwargs):
        """
        Signs and generates the query string URL parameters to use when making a request.

        If the `client_secret` key is provided, then it will be automatically excluded from the result.

        `token (string)`: The one-time-use token. **Required**.

        `page (string)`: The WePay URL to access. **Required**.

        `redirect_uri (string)`: The partner URL to return to once the action is completed. **Required**.

        `return (string)`: The query string parameters to append to the end of a URL.
        """

        kwargs.pop('client_secret', None)

        signed_token = self.sign(**kwargs)
        kwargs['client_id'] = self.client_id
        kwargs['stoken'] = signed_token
        qsa = []

        payload_keys = list(six.viewkeys(kwargs))
        payload_keys.sort()

        for key in payload_keys:
            qsa.append("{}={}".format(key, kwargs[key]))

        return "&".join(qsa)

    # --------------------------------------------------------------------------
    # Private

    def __create_string_to_sign(self, scope, context):
        """
        Creates the string-to-sign based on a variety of factors.

        `scope (string)`: The results of a call to the `__create_scope()` method.

        `context (string)`: The results of a call to the `__create_context()` method.

        `return (string)`: The final string to be signed.
        """

        scope_hash = hashlib.new(self.hash_algo().name, scope.encode('utf-8')).hexdigest()
        context_hash = hashlib.new(self.hash_algo().name, context.encode('utf-8')).hexdigest()

        return "SIGNER-HMAC-{hash_algo}\n{self_key}\n{client_id}\n{scope_hash}\n{context_hash}".format(
            hash_algo=self.hash_algo().name.upper(),
            self_key=self.self_key,
            client_id=self.client_id,
            scope_hash=scope_hash,
            context_hash=context_hash
        )

    @staticmethod
    def __create_context(**kwargs):
        """
        An array of key-value pairs representing the data that you want to sign.
        All values must be `scalar`.

        `kwargs (dictionary)`: The data that you want to sign.

        `self_key (string)`: A string which identifies the signing party and adds additional
            entropy. The default value is `WePay`.

        `return (string)`: A canonical string representation of the data to sign.
        """

        canonical_payload = []

        for k in six.viewkeys(kwargs):
            val = "{}".format(kwargs[k]).lower()
            key = "{}".format(k).lower()
            canonical_payload.append("{}={}\n".format(key, val))

        canonical_payload.sort()

        sorted_keys = list(six.viewkeys(kwargs))
        sorted_keys.sort()

        signed_headers_string = ";".join(sorted_keys)
        canonical_payload_string = "".join(canonical_payload) + "\n" + signed_headers_string

        return canonical_payload_string

    def __get_signing_salt(self):
        """
        Gets the salt value that should be used for signing.

        `return (string,bytearray)`: The signing salt.
        """

        self_key_sign = hmac.new(
            six.b(self.client_secret),
            six.u(self.self_key).encode('utf-8'),
            self.hash_algo
        ).digest()

        client_id_sign = hmac.new(
            self_key_sign,
            six.u(self.client_id).encode('utf-8'),
            self.hash_algo
        ).digest()

        signer_sign = hmac.new(
            client_id_sign,
            six.u('signer').encode('utf-8'),
            self.hash_algo
        ).digest()

        return signer_sign

    def __create_scope(self):
        """
        Creates the "scope" in which the signature is valid.

        `return (string)`: The string which represents the scope in which the signature is valid.
        """

        return "{self_key}/{client_id}/signer".format(
            self_key=self.self_key,
            client_id=self.client_id
        )

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2015-2016 WePay.

Based on a stripped-down version of the AWS Signature v4 implementation.

http://opensource.org/licenses/Apache2.0
"""

from __future__ import print_function
import unittest
import nose2
from wepay.signer import Signer

# Test data
DEFAULT_CLIENT_ID = 12173158495
DEFAULT_CLIENT_SECRET = '1594122c5c36f438f8ba'
DEFAULT_SIGNATURE = ('c2de34c15cd76f797cf80781747da3874639a827a4cb79dcd862cc17b35cf2e2c721ea7d49ab'
                     '9f60590d637ae0f51fd4ed8ddb551b922e0cd7e35a13b86de360')
DEFAULT_PAGE = 'https://wepay.com/account/12345'
DEFAULT_REDIRECT_URI = 'https://partnersite.com/home'
DEFAULT_QS = 'client_id={}&page={}&redirect_uri={}&stoken={}&token={}'
DEFAULT_TOKEN = '10c936ca-5e7c-508b-9e60-b211c20be9bc'


class Test(unittest.TestCase):
    """Unit tests for the wepay.signer.Signer class."""

    def setUp(self):
        """Instantiate the class."""
        self.signer = Signer(DEFAULT_CLIENT_ID, DEFAULT_CLIENT_SECRET)

    def test_get_self_key(self):
        """Make sure we can read the self_key property."""
        self.assertEqual('WePay', self.signer.self_key)

    def test_get_client_key(self):
        """Make sure we can read the client_key property."""
        self.assertEqual("{}".format(DEFAULT_CLIENT_ID), self.signer.client_id)

    def test_get_client_secret(self):
        """Make sure we can read the client_secret property."""
        self.assertEqual("{}".format(DEFAULT_CLIENT_SECRET), self.signer.client_secret)

    def test_get_hash_algo(self):
        """Make sure we can read the hash_algo property."""
        self.assertEqual('sha512', self.signer.hash_algo().name)

    def test_sign(self):
        """Generate a new signature and ensure it matches what is expected with the same inputs."""
        signature = self.signer.sign(
            page=DEFAULT_PAGE,
            redirect_uri=DEFAULT_REDIRECT_URI,
            token=DEFAULT_TOKEN
        )

        self.assertEqual(DEFAULT_SIGNATURE, signature)

    def test_query_string_params(self):
        """Generate a new querystring with signature and ensure it matches what is expected with the same inputs."""
        querystring = self.signer.generate_query_string_params(
            page=DEFAULT_PAGE,
            redirect_uri=DEFAULT_REDIRECT_URI,
            token=DEFAULT_TOKEN
        )

        self.assertEqual(
            DEFAULT_QS.format(DEFAULT_CLIENT_ID, DEFAULT_PAGE, DEFAULT_REDIRECT_URI, DEFAULT_SIGNATURE, DEFAULT_TOKEN),
            querystring
        )

    def test_query_string_params_client_secret(self):
        """Generate a new querystring with signature and ensure it matches what is expected with the same inputs."""
        querystring = self.signer.generate_query_string_params(
            page=DEFAULT_PAGE,
            redirect_uri=DEFAULT_REDIRECT_URI,
            token=DEFAULT_TOKEN,
            client_id=DEFAULT_CLIENT_ID,
            client_secret=DEFAULT_CLIENT_SECRET
        )

        self.assertEqual(
            DEFAULT_QS.format(DEFAULT_CLIENT_ID, DEFAULT_PAGE, DEFAULT_REDIRECT_URI, DEFAULT_SIGNATURE, DEFAULT_TOKEN),
            querystring
        )

if __name__ == '__main__':
    nose2.main()

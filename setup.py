from setuptools import setup, find_packages

version = open('VERSION').read()

requires = [
    'autoflake==0.6.6',
    'autopep8==1.2.4',
    'pylint==1.6.4',
    'six==1.10.0',
]

setup(
    name='wepay-signer',
    license="Apache License 2.0",
    author='WePay',
    author_email='api@wepay.com',
    url="https://github.com/wepay/signer-python",
    install_requires=requires,
    version=version,
    packages=find_packages(exclude=['tests*']),
    description='A Modern Python 2/3 SDK for signing WePay requests.',
    long_description=open('README.rst').read(),
    keywords='wepay signer',
    test_suite='nose2.collector.collector',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)

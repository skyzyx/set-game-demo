from setuptools import setup, find_packages

version = open('VERSION').read()

requires = [
    'autoflake==0.6.6',
    'autopep8==1.2.4',
    'pylint==1.6.4',
    'six==1.10.0',
]

setup(
    name='skyzyx-set-game-demo',
    license="Apache License 2.0",
    author='Ryan Parman',
    author_email='ryan@ryanparman.com',
    url="https://github.com/skyzyx/set-game-demo",
    install_requires=requires,
    version=version,
    packages=find_packages(exclude=['tests*']),
    description='Simple demo of the game of Set.',
    long_description=open('README.rst').read(),
    keywords='set demo game',
    test_suite='nose2.collector.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
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

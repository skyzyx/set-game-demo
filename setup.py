from setuptools import setup, find_packages

# Read the contents of README.rst. Generate this with `make readme`.
readme = open('README.rst').read()

# Read the contents of VERSION. Generate this with `make version`.
version = open('VERSION').read()

# Runtime requirements (which are different from development requirements)
requires = [
    'autoflake>=0.6.6,<1.0',
    'autopep8>=1.2.4,<2.0',
    'prettytable>=0.7.2,<1.0',
    'pylint>=1.6.4,<2.0',
    'six>=1.10.0,<2.0',
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
    long_description=readme,
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
    entry_points={
        'console_scripts': [
            'set-game-demo=set_game_demo:main',
        ],
    },
)

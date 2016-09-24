# Set

[![Source](http://img.shields.io/badge/source-skyzyx/set-game-demo-blue.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo)
#[![Downloads](https://img.shields.io/pypi/dm/wepay-signer.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/releases)
[![Release](https://img.shields.io/github/release/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/releases)
#[![Pypi Release](https://img.shields.io/pypi/v/wepay-signer.svg?style=flat-square)](https://pypi.python.org/pypi/wepay-signer)
[![Open Issues](http://img.shields.io/github/issues/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/issues)
[![Build Status](http://img.shields.io/travis/skyzyx/set-game-demo/master.svg?style=flat-square)](https://travis-ci.org/skyzyx/set-game-demo)
#[![Implementation](https://img.shields.io/pypi/implementation/wepay-signer.svg?style=flat-square)](https://python.org)
#[![Python Versions](https://img.shields.io/pypi/pyversions/wepay-signer.svg?style=flat-square)](https://python.org)
#[![Package Format](https://img.shields.io/pypi/format/wepay-signer.svg?style=flat-square)](http://pythonwheels.com)
#[![Stability](https://img.shields.io/pypi/status/wepay-signer.svg?style=flat-square)](https://pypi.python.org/pypi/wepay-signer)
[![Coverage Status](http://img.shields.io/coveralls/skyzyx/set-game-demo/master.svg?style=flat-square)](https://coveralls.io/r/skyzyx/set-game-demo?branch=master)
[![Code Climate](http://img.shields.io/codeclimate/github/skyzyx/set-game-demo.svg?style=flat-square)](https://codeclimate.com/github/skyzyx/set-game-demo)
[![Code Quality](http://img.shields.io/scrutinizer/g/skyzyx/set-game-demo.svg?style=flat-square)](https://scrutinizer-ci.com/g/skyzyx/set-game-demo)
[![License](https://img.shields.io/github/license/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/blob/master/LICENSE.rst)
[![Author](http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square)](https://github.com/skyzyx)

"Set" is a card game where a group of players try to identify a "set" of cards from those placed face-up on a table.

This project uses [Semantic Versioning](http://semver.org) for managing backwards-compatibility.

* [API Reference](https://skyzyx.github.io/set-game-demo/)


## The Game
### Game Rules

Each card has an image on it with 4 orthogonal attributes:

* Color (red, green, or purple)
* Shape (diamond, squiggle, or oval)
* Shading (solid, empty, or striped)
* Number (one, two, or three)

Three cards are a part of a set if, for each property, the values are all the same or all different.

For example:

* The cards "two red solid squiggles", "one green solid diamond", "three purple solid ovals" would make up a set. (number, shape, and color are different, shading is the same)
* The cards "two red solid squiggles", "one green solid squiggles", "three purple solid ovals" would not make up a set, because shape is the same on two cards, but different on the third.
* A game of Set starts by dealing 12 cards, face-up. When a player sees three cards that make up a set, they yell "Set!" and grab the cards. New cards are dealt from the deck to replace them.
* If no player can find a set, three more cards are dealt (to make 15, then 18, then 21…)
* The game is over when there are no cards left in the deck, and no sets left on the table. The player with the most sets wins.

### Game Requirements

Your task is to model the game in code, and implement the following methods:

* A method that takes three cards, and determines whether the three cards make a set
* A method that given a "board" of cards, will either find a set, or determine if there are no sets on the table
* A method that will play an entire game of Set, from beginning to end, and return a list of each valid sets you removed from the board.

For this last method, there will be multiple correct solutions, but any valid list of sets is fine.

### Problem Parameters


### Logic


## Requirements

* Python 2.7, 3.3+, Pypy
* Pip
* VirtualEnv is recommended, but not required
* [Chag]

## Installation

```bash
pip install skyzyx-set-game-demo
```

And either include it in your scripts:

```python
from set_game_demo import Game
```

…or run it from the command line.

```bash
# Application help
set-game-demo -h
```

## Usage/Examples


## Known Issues


## Future Improvements


## Development

* You can develop in any supported version of Python.

* Using [pyenv] to manage your Pythons is _highly-recommended_. Testing locally **depends** on it.

* Install [VirtualEnv] for your development environment, and _activate_ the environment.

  ```bash
  pip install virtualenv
  virtualenv .vendor
  source .vendor/bin/activate
  ```

* Install the `requirements.txt`.

  ```bash
  pip install -r requirements.txt
  ```

* When you make changes, make sure that you run the linter and fix anything that's broken.

  ```bash
  make lint
  ```


## Testing

We use [tox] to handle local testing across multiple versions of Python. We install multiple versions of Python at a time with [pyenv].

Testing occurs against the following versions:

* Python 2.7
* Python 3.3
* Python 3.4
* Python 3.5
* Python 3.6 (dev)
* Pypy (≈2.7.10)
* Pypy3 (≈3.2.5)

To begin…

1. Install [pyenv] on your own before running tests.

1. You need to install all of the supported versions of Python. (This will take a while.) If you would prefer to install your own copies of the supported Python versions (listed above), feel free to manage them yourself.

   ```bash
   make install-python
   ```

1. You can run the tests as follows:

   ```bash
   make test
   ```


## API Reference

### Building local docs

```bash
make docs
open docs/set/index.html
```

### Building and pushing docs

```bash
make pushdocs
```

Docs can be viewed at <https://skyzyx.github.io/set-game-demo/>.


## Deploying

1. The `Makefile` (yes, `Makefile`) has a series of commands to simplify the development and deployment process.
1. Also install [Chag]. This is used for managing the `CHANGELOG` and annotating the Git release correctly.

### Updating the CHANGELOG

Make sure that the `CHANGELOG.md` is human-friendly. See http://keepachangelog.com if you don’t know how.

### `make`

Running `make` by itself will show you a list of available sub-commands.

```bash
$ make
all
build
clean
docs
install
install-python
lint
push
pushdocs
readme
tag
test
version
```

### `make readme`

If you make changes to `README.md`, then this will use [Pandoc] to output a `README.rst` file in the [reStructuredText] format used by [distutils], [Sphinx] and most of the Python community.

You must have [Pandoc] installed on your local system.

> **NOTE:** Initial install via `brew install pandoc` takes about 8–10 hours. Updates are much faster. [Using the installer](https://github.com/jgm/pandoc/releases) is **much** faster for initial installation, but updates are entirely manual.

### `make version`

Sets the version number that will be used by other `make` tasks related to packaging and bundling.

### `make tag`

This will make sure that the `CHANGELOG.md` is properly datestamped, add the CHANGELOG contents to the Git commit message, commit them, then create a Git commit which can be pushed upstream.

### `make buildpip`

This will bundle-up your package in preparation for uploading to [Pypi].

### `make pushpip`

This will take your bundled package and upload it securely to [Pypi] using the `twine` package.

### Drafting a GitHub release

1. Go to https://github.com/skyzyx/set-game-demo/tags
1. Find the new tag that you just pushed. Click the ellipsis (`…`) to see the commit notes. Copy these.
1. To the right, choose _Add release notes_. Your _Tag version_ should be pre-filled.
1. The _Release title_ should match your _Tag version_.
1. Inside _Describe this release_, paste the notes that you copied on the previous page.
1. Choose _Publish release_.
1. Your release should now be the latest. https://github.com/skyzyx/set-game-demo/releases/latest


## Contributing
Here's the process for contributing:

1. Fork Signer to your GitHub account.
2. Clone your GitHub copy of the repository into your local workspace.
3. Write code, fix bugs, and add tests with 100% code coverage.
4. Commit your changes to your local workspace and push them up to your GitHub copy.
5. You submit a GitHub pull request with a description of what the change is.
6. The contribution is reviewed. Maybe there will be some banter back-and-forth in the comments.
7. If all goes well, your pull request will be accepted and your changes are merged in.


## Authors, Copyright & Licensing

* Copyright (c) 2016 [Ryan Parman](http://github.com/skyzyx)

See also the list of [contributors](https://github.com/skyzyx/set-game-demo/graphs/contributors) who participated in this project.

Licensed for use under the terms of the [Apache 2.0] license.

  [Apache 2.0]: http://opensource.org/licenses/Apache-2.0
  [Chag]: https://github.com/mtdowling/chag
  [distutils]: https://docs.python.org/3/library/distutils.html
  [Pandoc]: http://pandoc.org
  [pyenv-virtualenvwrapper]: https://github.com/yyuu/pyenv-virtualenvwrapper
  [pyenv]: https://github.com/yyuu/pyenv
  [reStructuredText]: http://docutils.sourceforge.net/rst.html
  [Sphinx]: http://www.sphinx-doc.org
  [tox]: https://tox.readthedocs.io
  [VirtualEnv]: https://virtualenv.pypa.io/en/stable/
  [Pypi]: https://pypi.python.org/pypi

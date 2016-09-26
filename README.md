# Set

[![Source](http://img.shields.io/badge/source-skyzyx/set-game-demo-blue.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo)
[![Downloads](https://img.shields.io/pypi/dm/skyzyx-set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/releases)
[![Release](https://img.shields.io/github/release/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/releases)
[![Pypi Release](https://img.shields.io/pypi/v/skyzyx-set-game-demo.svg?style=flat-square)](https://pypi.python.org/pypi/skyzyx-set-game-demo)
[![Open Issues](http://img.shields.io/github/issues/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/issues)
[![Build Status](http://img.shields.io/travis/skyzyx/set-game-demo/master.svg?style=flat-square)](https://travis-ci.org/skyzyx/set-game-demo)
[![Implementation](https://img.shields.io/pypi/implementation/skyzyx-set-game-demo.svg?style=flat-square)](https://python.org)
[![Python Versions](https://img.shields.io/pypi/pyversions/skyzyx-set-game-demo.svg?style=flat-square)](https://python.org)
[![Package Format](https://img.shields.io/pypi/format/skyzyx-set-game-demo.svg?style=flat-square)](http://pythonwheels.com)
[![Stability](https://img.shields.io/pypi/status/skyzyx-set-game-demo.svg?style=flat-square)](https://pypi.python.org/pypi/skyzyx-set-game-demo)
[![Coverage Status](http://img.shields.io/coveralls/skyzyx/set-game-demo/master.svg?style=flat-square)](https://coveralls.io/r/skyzyx/set-game-demo?branch=master)
[![Code Climate](http://img.shields.io/codeclimate/github/skyzyx/set-game-demo.svg?style=flat-square)](https://codeclimate.com/github/skyzyx/set-game-demo)
[![Code Quality](http://img.shields.io/scrutinizer/g/skyzyx/set-game-demo.svg?style=flat-square)](https://scrutinizer-ci.com/g/skyzyx/set-game-demo)
[![License](https://img.shields.io/github/license/skyzyx/set-game-demo.svg?style=flat-square)](https://github.com/skyzyx/set-game-demo/blob/master/LICENSE.md)
[![Author](http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square)](https://github.com/skyzyx)

"Set" is a card game where a group of players try to identify a _Set_ of cards from those placed face-up on a table.

This project uses [Semantic Versioning](http://semver.org) for managing backwards-compatibility.

* [API Reference](https://skyzyx.github.io/set-game-demo/)


## The Game

### Core Concepts

* Each _Card_ has 4 _Properties_: color, shape, shading, and number.
* The _Deck_ is a collection of all of the _Cards_.
* The _Board_ is a subset of the _Deck_, containing only the cards that are currently in-play.
* A _Set_ is a collection of 3 cards which meet certain criteria (discussed below). When a _Set_ is found in-play on the _Board_, the _Set_ is removed from play and logged as such.
* The _Game_ encapsulates all of these concepts and keeps track of them.

### Game Rules

Each _Card_ has an image on it with 4 orthogonal attributes:

* Color (red, green, or purple)
* Shape (diamond, squiggle, or oval)
* Shading (solid, empty, or striped)
* Number (one, two, or three)

Three _Cards_ are a part of a _Set_ if, for each _Property_, the values are all the same or all different.

For example:

* The _Cards_ "two red solid squiggles", "one green solid diamond", "three purple solid ovals" would make up a
  _Set_. (number, shape, and color are different, shading is the same)
* The _Cards_ "two red solid squiggles", "one green solid squiggles", "three purple solid ovals" would not make up a
  _Set_, because shape is the same on two _Cards_, but different on the third.
* A _Game_ of "Set" starts by dealing 12 _Cards_, face-up. When a player sees three _Cards_ that make up a _Set_,
  they yell "Set!" and grab the _Cards_. New _Cards_ are dealt from the _Deck_ to replace them.
* If no player can find a _Set_, three more _Cards_ are dealt (to make 15, then 18, then 21...)
* The _Game_ is over when there are no _Cards_ left in the _Deck_, and no _Sets_ left on the table. The player with
  the most _Sets_ wins.

### Game Requirements

Your task is to model the _Game_ in code, and implement the following methods:

* A method that takes three _Cards_, and determines whether the three _Cards_ make a _Set_.
* A method that given a _Board_ of _Cards_, will either find a _Set_, or determine that there are no _Sets_ on the
  table.
* A method that will play an entire _Game_ of "Set", from beginning to end, and return a list of each valid _Sets_
  you removed from the _Board_.

For this last method, there will be multiple correct solutions, but any valid list of _Sets_ is fine.

### Assumptions

> _“Three cards are a part of a set if, for each property, the values are all the same or all different.”_

This is phrased ambiguously, and the examples given lead me to believe that the following is a more specific description of the rules.

* Take 3 cards and look at each of their properties one-by-one.
* If all cards have a different value for that property OR all cards have the same value for that property, then it _may_ be a set.
* If _any_ properties of step 2 fail the test, then the group is not a set.

### Problem Parameters

* This problem uses mathematical _combinations_ (as opposed to _permutations_). This results in 81 combinations (`3^4`).
* Any failure of being a _Set_ means that the group is not a set, so fail as early as possible and move-on.


### Logic

(Whereas “_Combination_” refers to the [mathematical concept](https://en.wikipedia.org/wiki/Combination).)

1. Create the deck of available cards by ensuring that every card is unique, and that all _Combinations_ of properties are represented. Also, shuffle the deck by default.
1. Deal 12 cards to the _Board_.
1. Calculate all possible _Combinations_ of the cards on the _Board_, in groups of 3.
1. Iterate over each _Combination_, applying logic to determine whether or not this _Combination_ represents a _Set_.
1. Collect the _Sets_ by removing the _Cards_ which are determined to be part of a _Set_.
1. When no more _Sets_ can be found, deal another 3 _Cards_ from the _Deck_.
1. Repeat steps 3–6 until the _Deck_ is empty.

## Requirements

* Python 2.7, 3.3+, Pypy
* Pip
* VirtualEnv is recommended, but not required


## Installation

```bash
# Install from Pypi
pip install skyzyx-set-game-demo

# Install from local code
pip install -e .
```

And either include it in your scripts:

```python
from set_game_demo import SetGame
```

…or run it from the command line.

```bash
# Application help
set-game-demo -h
```

## Usage/Examples

From the Python REPL or a Python script…

```python
from __future__ import print_function
from set_game_demo import SetGame

# Initialize the game.
game = SetGame()

# Chatty, interactive version of the game.
game.play()

# Quiet version of the game. Good for code.
discovered, sets = game.play_quiet()
print("Sets discovered: {}".format(discovered))
for set in sets:
    game.display_cards(set)
```

From the Terminal…

```bash
# Chatty, interactive version of the game.
set-game-demo

# Quiet version of the game.
set-game-demo --quiet
```

## Known Issues

* In a final release, it would be wise to update the `requirements.txt` to allow for ranges of known-good versions instead of locking to one specific version.
    * Conversely, if this is the sole project running in this virtual environment, locking to a specific known-good version ensures fewer version-compatibility issues.


## Future Improvements

* Update the `test_deal` unit test to verify that we do not attempt to deal a larger number of cards than the deck contains (couldn't quite figure out the right way to call `assertRaises()` from the `unittest` package through the `nose2` interface).
* Support multiple _Players_ who can collect sets and compete for scores.


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
* Python 3.6 (beta)
* Pypy (≈2.7.10)
* Pypy3 (≈3.2.5)

To begin…

1. Install [pyenv] on your own before running tests.

1. You need to install all of the supported versions of Python. (This will take a while.) If you would prefer to install your own copies of the supported Python versions (listed above), feel free to manage them yourself.

   ```bash
   pyenv install 3.6.0b1 && \
   pyenv install 3.5.2 && \
   pyenv install 3.4.5 && \
   pyenv install 3.3.6 && \
   pyenv install 2.7.12 && \
   pyenv install pypy-5.3.1 && \
   pyenv install pypy3-2.4.0 && \
   pyenv rehash && \
   eval "$(pyenv init -)" && \
   pyenv global system 3.6.0b1 3.5.2 3.4.5 3.3.6 2.7.12 pypy-5.3.1 pypy3-2.4.0
   ```

   To verify that the installation and configuration were successful, you can run `pyenv versions`. You should see a `*` character in front of every version that we just installed.

   ```bash
   $ pyenv versions
   * system (set by ~/.pyenv/version)
   * 2.7.12 (set by ~/.pyenv/version)
   * 3.3.6 (set by ~/.pyenv/version)
   * 3.4.5 (set by ~/.pyenv/version)
   * 3.5.2 (set by ~/.pyenv/version)
   * 3.6.0b1 (set by ~/.pyenv/version)
   * pypy-5.3.1 (set by ~/.pyenv/version)
   * pypy3-2.4.0 (set by ~/.pyenv/version)
   ```

1. The following command will package-up your module and install it locally, then run `nose2` to execute the tests in the _default system Python_.

   ```bash
   make test
   ```


1. After you've run that, you can then execute the tests in all supported versions of Python with the following:

   ```bash
   tox
   ```

## API Reference

### Building local docs

```bash
make docs
open docs/set_game_demo/index.html
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
buildpip
clean
docs
lint
pushdocs
pushpip
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

Set
===

| |Source|
| @\ |Downloads|
| |Release|
| @\ |Pypi Release|
| |Open Issues|
| |Build Status|
| @\ |Implementation|
| @\ |Python Versions|
| @\ |Package Format|
| @\ |Stability|
| |Coverage Status|
| |Code Climate|
| |Code Quality|
| |License|
| |Author|

"Set" is a card game where a group of players try to identify a "set" of
cards from those placed face-up on a table.

This project uses `Semantic Versioning <http://semver.org>`__ for
managing backwards-compatibility.

-  `API Reference <https://skyzyx.github.io/set-game-demo/>`__

The Game
--------

Core Concepts
~~~~~~~~~~~~~

-  Each *Card* has 4 *Properties*: color, shape, shading, and number.
-  The *Deck* is a collection of all of the *Cards*.
-  The *Board* is a subset of the *Deck*, containing only the cards that
   are currently in-play.
-  A *Set* is a collection of 3 cards which meet certain criteria
   (discussed below). When a *Set* is found in-play on the *Board*, the
   *Set* is removed from play and logged as such.
-  The *Game* encapsulates all of these concepts and keeps track of
   them.

Game Rules
~~~~~~~~~~

Each card has an image on it with 4 orthogonal attributes:

-  Color (red, green, or purple)
-  Shape (diamond, squiggle, or oval)
-  Shading (solid, empty, or striped)
-  Number (one, two, or three)

Three cards are a part of a set if, for each property, the values are
all the same or all different.

For example:

-  The cards "two red solid squiggles", "one green solid diamond",
   "three purple solid ovals" would make up a set. (number, shape, and
   color are different, shading is the same)
-  The cards "two red solid squiggles", "one green solid squiggles",
   "three purple solid ovals" would not make up a set, because shape is
   the same on two cards, but different on the third.
-  A game of Set starts by dealing 12 cards, face-up. When a player sees
   three cards that make up a set, they yell "Set!" and grab the cards.
   New cards are dealt from the deck to replace them.
-  If no player can find a set, three more cards are dealt (to make 15,
   then 18, then 21…)
-  The game is over when there are no cards left in the deck, and no
   sets left on the table. The player with the most sets wins.

Game Requirements
~~~~~~~~~~~~~~~~~

Your task is to model the game in code, and implement the following
methods:

-  A method that takes three cards, and determines whether the three
   cards make a set
-  A method that given a "board" of cards, will either find a set, or
   determine if there are no sets on the table
-  A method that will play an entire game of Set, from beginning to end,
   and return a list of each valid sets you removed from the board.

For this last method, there will be multiple correct solutions, but any
valid list of sets is fine.

Assumptions
~~~~~~~~~~~

    *“Three cards are a part of a set if, for each property, the values
    are all the same or all different.”*

This is phrased ambiguously, and the examples given lead me to believe
that the following is a better description of the rules.

-  Take 3 cards and look at each of their properties one-by-one.
-  If all cards have a different value for that property OR all cards
   have the same value for that property, then it *may* be a set.
-  If *any* properties of step 2 fail the test, then the group is not a
   set.

Problem Parameters
~~~~~~~~~~~~~~~~~~

-  This problem uses mathematical *combinations* (as opposed to
   *permutations*). This results in 81 combinations (``3^4``).
-  Any failure of being a *Set* means that the group is not a set, so
   fail as early as possible and move-on.

Logic
~~~~~

#. Create the deck of available cards by ensuring that every card is
   unique, and that all combinations of properties are represented.
   Also, shuffle the deck by default.
#. Deal 12 cards to the board.

Requirements
------------

-  Python 2.7, 3.3+, Pypy
-  Pip
-  VirtualEnv is recommended, but not required
-  `Chag <https://github.com/mtdowling/chag>`__

Installation
------------

.. code:: bash

    pip install skyzyx-set-game-demo

And either include it in your scripts:

.. code:: python

    from set_game_demo import SetGame

…or run it from the command line.

.. code:: bash

    # Application help
    set-game-demo -h

Usage/Examples
--------------

Known Issues
------------

-  This uses an implementation of ``SimpleNamespace`` that is written in
   Python instead of C, which is slower than the native
   ``SimpleNamespace`` class, but has compatibility with Python 2.7.
-  In a final release, it would be wise to update the
   ``requirements.txt`` to allow for ranges of known-good versions
   instead of locking to one specific version.

   -  Conversely, if this is the sole project running in this virtual
      environment, locking to a specific known-good version ensures
      fewer version-compatibility issues.

Future Improvements
-------------------

-  Update ``SimpleNamespace`` to leverage the ``six`` module for passing
   the C version of the class to Python 3.3+.
-  Update the ``test_deal`` unit test to verify that we do not attempt
   to deal a larger number of cards than the deck contains (couldn't
   quite figure out the right way to call ``assertRaises()`` from the
   ``unittest`` package through the ``nose2`` interface).

Development
-----------

-  You can develop in any supported version of Python.

-  Using `pyenv <https://github.com/yyuu/pyenv>`__ to manage your
   Pythons is *highly-recommended*. Testing locally **depends** on it.

-  Install `VirtualEnv <https://virtualenv.pypa.io/en/stable/>`__ for
   your development environment, and *activate* the environment.

``bash   pip install virtualenv   virtualenv .vendor   source .vendor/bin/activate``

-  Install the ``requirements.txt``.

``bash   pip install -r requirements.txt``

-  When you make changes, make sure that you run the linter and fix
   anything that's broken.

``bash   make lint``

Testing
-------

We use `tox <https://tox.readthedocs.io>`__ to handle local testing
across multiple versions of Python. We install multiple versions of
Python at a time with `pyenv <https://github.com/yyuu/pyenv>`__.

Testing occurs against the following versions:

-  Python 2.7
-  Python 3.3
-  Python 3.4
-  Python 3.5
-  Python 3.6 (beta)
-  Pypy (≈2.7.10)
-  Pypy3 (≈3.2.5)

To begin…

#. Install `pyenv <https://github.com/yyuu/pyenv>`__ on your own before
   running tests.

#. You need to install all of the supported versions of Python. (This
   will take a while.) If you would prefer to install your own copies of
   the supported Python versions (listed above), feel free to manage
   them yourself.

``bash    pyenv install 3.6.0b1 && \    pyenv install 3.5.2 && \    pyenv install 3.4.5 && \    pyenv install 3.3.6 && \    pyenv install 2.7.12 && \    pyenv install pypy-5.3.1 && \    pyenv install pypy3-2.4.0 && \    pyenv rehash && \    eval "$(pyenv init -)" && \    pyenv global system 3.6.0b1 3.5.2 3.4.5 3.3.6 2.7.12 pypy-5.3.1 pypy3-2.4.0``

To verify that the installation and configuration were successful, you
can run ``pyenv versions``. You should see a ``*`` character in front of
every version that we just installed.

``bash    $ pyenv versions    * system (set by ~/.pyenv/version)    * 2.7.12 (set by ~/.pyenv/version)    * 3.3.6 (set by ~/.pyenv/version)    * 3.4.5 (set by ~/.pyenv/version)    * 3.5.2 (set by ~/.pyenv/version)    * 3.6.0b1 (set by ~/.pyenv/version)    * pypy-5.3.1 (set by ~/.pyenv/version)    * pypy3-2.4.0 (set by ~/.pyenv/version)``

#. The following command will package-up your module and install it
   locally, then run ``nose2`` to execute the tests in the *default
   system Python*.

``bash    make test``

#. After you've run that, you can then execute the tests in all
   supported versions of Python with the following:

``bash    tox``

API Reference
-------------

Building local docs
~~~~~~~~~~~~~~~~~~~

.. code:: bash

    make docs
    open docs/set/index.html

Building and pushing docs
~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    make pushdocs

Docs can be viewed at https://skyzyx.github.io/set-game-demo/.

Deploying
---------

#. The ``Makefile`` (yes, ``Makefile``) has a series of commands to
   simplify the development and deployment process.
#. Also install `Chag <https://github.com/mtdowling/chag>`__. This is
   used for managing the ``CHANGELOG`` and annotating the Git release
   correctly.

Updating the CHANGELOG
~~~~~~~~~~~~~~~~~~~~~~

Make sure that the ``CHANGELOG.md`` is human-friendly. See
http://keepachangelog.com if you don’t know how.

``make``
~~~~~~~~

Running ``make`` by itself will show you a list of available
sub-commands.

.. code:: bash

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

``make readme``
~~~~~~~~~~~~~~~

If you make changes to ``README.md``, then this will use
`Pandoc <http://pandoc.org>`__ to output a ``README.rst`` file in the
`reStructuredText <http://docutils.sourceforge.net/rst.html>`__ format
used by
`distutils <https://docs.python.org/3/library/distutils.html>`__,
`Sphinx <http://www.sphinx-doc.org>`__ and most of the Python community.

You must have `Pandoc <http://pandoc.org>`__ installed on your local
system.

    **NOTE:** Initial install via ``brew install pandoc`` takes about
    8–10 hours. Updates are much faster. `Using the
    installer <https://github.com/jgm/pandoc/releases>`__ is **much**
    faster for initial installation, but updates are entirely manual.

``make version``
~~~~~~~~~~~~~~~~

Sets the version number that will be used by other ``make`` tasks
related to packaging and bundling.

``make tag``
~~~~~~~~~~~~

This will make sure that the ``CHANGELOG.md`` is properly datestamped,
add the CHANGELOG contents to the Git commit message, commit them, then
create a Git commit which can be pushed upstream.

``make buildpip``
~~~~~~~~~~~~~~~~~

This will bundle-up your package in preparation for uploading to
`Pypi <https://pypi.python.org/pypi>`__.

``make pushpip``
~~~~~~~~~~~~~~~~

This will take your bundled package and upload it securely to
`Pypi <https://pypi.python.org/pypi>`__ using the ``twine`` package.

Drafting a GitHub release
~~~~~~~~~~~~~~~~~~~~~~~~~

#. Go to https://github.com/skyzyx/set-game-demo/tags
#. Find the new tag that you just pushed. Click the ellipsis (``…``) to
   see the commit notes. Copy these.
#. To the right, choose *Add release notes*. Your *Tag version* should
   be pre-filled.
#. The *Release title* should match your *Tag version*.
#. Inside *Describe this release*, paste the notes that you copied on
   the previous page.
#. Choose *Publish release*.
#. Your release should now be the latest.
   https://github.com/skyzyx/set-game-demo/releases/latest

Contributing
------------

Here's the process for contributing:

#. Fork Signer to your GitHub account.
#. Clone your GitHub copy of the repository into your local workspace.
#. Write code, fix bugs, and add tests with 100% code coverage.
#. Commit your changes to your local workspace and push them up to your
   GitHub copy.
#. You submit a GitHub pull request with a description of what the
   change is.
#. The contribution is reviewed. Maybe there will be some banter
   back-and-forth in the comments.
#. If all goes well, your pull request will be accepted and your changes
   are merged in.

Authors, Copyright & Licensing
------------------------------

-  Copyright (c) 2016 `Ryan Parman <http://github.com/skyzyx>`__

See also the list of
`contributors <https://github.com/skyzyx/set-game-demo/graphs/contributors>`__
who participated in this project.

Licensed for use under the terms of the `Apache
2.0 <http://opensource.org/licenses/Apache-2.0>`__ license.

.. |Source| image:: http://img.shields.io/badge/source-skyzyx/set-game-demo-blue.svg?style=flat-square
   :target: https://github.com/skyzyx/set-game-demo
.. |Downloads| image:: https://img.shields.io/pypi/dm/wepay-signer.svg?style=flat-square
   :target: https://github.com/skyzyx/set-game-demo/releases
.. |Release| image:: https://img.shields.io/github/release/skyzyx/set-game-demo.svg?style=flat-square
   :target: https://github.com/skyzyx/set-game-demo/releases
.. |Pypi Release| image:: https://img.shields.io/pypi/v/wepay-signer.svg?style=flat-square
   :target: https://pypi.python.org/pypi/wepay-signer
.. |Open Issues| image:: http://img.shields.io/github/issues/skyzyx/set-game-demo.svg?style=flat-square
   :target: https://github.com/skyzyx/set-game-demo/issues
.. |Build Status| image:: http://img.shields.io/travis/skyzyx/set-game-demo/master.svg?style=flat-square
   :target: https://travis-ci.org/skyzyx/set-game-demo
.. |Implementation| image:: https://img.shields.io/pypi/implementation/wepay-signer.svg?style=flat-square
   :target: https://python.org
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/wepay-signer.svg?style=flat-square
   :target: https://python.org
.. |Package Format| image:: https://img.shields.io/pypi/format/wepay-signer.svg?style=flat-square
   :target: http://pythonwheels.com
.. |Stability| image:: https://img.shields.io/pypi/status/wepay-signer.svg?style=flat-square
   :target: https://pypi.python.org/pypi/wepay-signer
.. |Coverage Status| image:: http://img.shields.io/coveralls/skyzyx/set-game-demo/master.svg?style=flat-square
   :target: https://coveralls.io/r/skyzyx/set-game-demo?branch=master
.. |Code Climate| image:: http://img.shields.io/codeclimate/github/skyzyx/set-game-demo.svg?style=flat-square
   :target: https://codeclimate.com/github/skyzyx/set-game-demo
.. |Code Quality| image:: http://img.shields.io/scrutinizer/g/skyzyx/set-game-demo.svg?style=flat-square
   :target: https://scrutinizer-ci.com/g/skyzyx/set-game-demo
.. |License| image:: https://img.shields.io/github/license/skyzyx/set-game-demo.svg?style=flat-square
   :target: https://github.com/skyzyx/set-game-demo/blob/master/LICENSE.rst
.. |Author| image:: http://img.shields.io/badge/author-@skyzyx-blue.svg?style=flat-square
   :target: https://github.com/skyzyx

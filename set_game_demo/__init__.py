# -*- coding: utf-8 -*-

"""
A simple demo of the game of "Set".

Copyright (c) 2016 [Ryan Parman](https://github.com/skyzyx).

<http://opensource.org/licenses/Apache2.0>
"""

from __future__ import print_function
import six


class Set(object):
    """
    "Set" is a card game where a group of players try to identify a "set" of cards from those placed face-up on a table.

    **Game Rules:**

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

    **Game Requirements:**

    Your task is to model the game in code, and implement the following methods:

    * A method that takes three cards, and determines whether the three cards make a set
    * A method that given a "board" of cards, will either find a set, or determine if there are no sets on the table
    * A method that will play an entire game of Set, from beginning to end, and return a list of each valid sets you removed from the board.

    For this last method, there will be multiple correct solutions, but any valid list of sets is fine.

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

        from set_game_demo import Set

    """

#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple demo of the game of "Set".

Copyright (c) 2016 [Ryan Parman](https://github.com/skyzyx).

<http://opensource.org/licenses/Apache2.0>
"""

from __future__ import print_function
import argparse
import collections
import itertools
import random
import six
from prettytable import PrettyTable


class SetGame(object):
    """
    "Set" is a card game where a group of players try to identify a _Set_ of cards from those placed face-up on a table.

    **Game Rules:**

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

    **Game Requirements:**

    Your task is to model the _Game_ in code, and implement the following methods:

    * A method that takes three _Cards_, and determines whether the three _Cards_ make a _Set_.
    * A method that given a _Board_ of _Cards_, will either find a _Set_, or determine that there are no _Sets_ on the
      table.
    * A method that will play an entire _Game_ of "Set", from beginning to end, and return a list of each valid _Sets_
      you removed from the _Board_.

    For this last method, there will be multiple correct solutions, but any valid list of _Sets_ is fine.

    **Compatibility:**

    Tested against the following Python versions:

    * Python 2.7
    * Python 3.3
    * Python 3.4
    * Python 3.5
    * Python 3.6 (beta)
    * Pypy (~2.7.10)
    * Pypy3 (~3.2.5)

    **Import:**

        from set_game_demo import SetGame

    """

    def __init__(self):
        """
        Constructs a new instance of this class.
        """

        self.colors = ["red", "green", "purple"]
        self.shapes = ["diamond", "squiggle", "oval"]
        self.shadings = ["solid", "empty", "striped"]
        self.numbers = ["one", "two", "three"]

        deck = []

        for color in self.colors:
            for shape in self.shapes:
                for shading in self.shadings:
                    for number in self.numbers:
                        card = {}
                        card["color"] = color
                        card["shape"] = shape
                        card["shading"] = shading
                        card["number"] = number

                        deck.append(card)

        random.shuffle(deck)

        self.deck = collections.deque(deck)
        self.board = []
        self.sets = []

    def deal(self, cards=12):
        """
        Deals a given number of cards from the top (front) of the deck.

        `cards (integer)`: The number of cards to deal out to the board. The default value is `12`.

        `return (cards[])`: A list (i.e., array) of objects representing cards.
        """

        out = []

        for _ in six.moves.range(cards):
            out.append(self.deck.popleft())

        return out

    def play(self):  # pragma: no cover
        """
        Play a (chatty) game of Set.

        `return (void)`
        """
        # pylint: disable=R0915

        # Introduction
        print("Welcome to a game of Set.")
        print()
        six.moves.input("=> Press any key to continue...")

        # First deal
        print()
        print("Dealing 12 cards onto the board.")
        self.board = self.deal(12)
        SetGame.display_cards(self.board)
        print()
        print("Cards on the board: {}".format(len(self.board)))
        print("Cards in the deck:  {}".format(len(self.deck)))
        print("Sets discovered:    {}".format(len(self.sets)))
        six.moves.input("=> Press any key to continue...")

        while len(self.deck) > 0:
            # Find sets
            print()
            sets = self.find_sets(self.board)
            print("Discovered {quantity}.".format(
                quantity=SetGame.plural(len(sets), "set", "sets")
            ))

            for i, sset in enumerate(sets):
                print()
                print("Set #{index}".format(index=(i + 1)))
                SetGame.display_cards(sset)

            print()
            print("These are the remaining {quantity} on the board.".format(
                quantity=SetGame.plural(len(self.board), "card", "cards")
            ))
            SetGame.display_cards(self.board)
            print()
            self.sets += sets
            six.moves.input("=> Press any key to continue...")

            # Deal 3 more cards
            print()
            self.board += self.deal(3)
            print("Dealing 3 more cards. You now have {quantity} on the board.".format(
                quantity=SetGame.plural(len(self.board), "card", "cards")
            ))
            SetGame.display_cards(self.board)
            print()
            print("Cards on the board: {}".format(len(self.board)))
            print("Cards in the deck:  {}".format(len(self.deck)))
            print("Sets discovered:    {}".format(len(self.sets)))
            six.moves.input("=> Press any key to continue...")

        # Find the very last set(s)
        print()
        sets = self.find_sets(self.board)
        print("Discovered {quantity}.".format(
            quantity=SetGame.plural(len(sets), "set", "sets")
        ))

        for i, sset in enumerate(sets):
            print()
            print("Set #{index}".format(index=(i + 1)))
            SetGame.display_cards(sset)

        print()
        print("These are the remaining {quantity} on the board.".format(
            quantity=SetGame.plural(len(self.board), "card", "cards")
        ))
        SetGame.display_cards(self.board)
        print()
        self.sets += sets
        six.moves.input("=> Press any key to continue...")

        # No more cards in the deck.
        print()
        print("There are no more cards left in the deck.")
        print()
        print("These are the {} that are left on the table.".format(
            SetGame.plural(len(self.board), "card", "cards")
        ))
        SetGame.display_cards(self.board)
        print()
        six.moves.input("=> Congratulations! You have completed the game. Press any key to see the results.")

        # Final score.
        print()
        print("You discovered {quantity}.".format(
            quantity=SetGame.plural(len(self.sets), "set", "sets")
        ))

        for i, sset in enumerate(self.sets):
            print()
            print("Set #{index}".format(index=(i + 1)))
            SetGame.display_cards(sset)

        # All done.
        print()
        print("Please play again!")
        print()

    def play_quiet(self):
        """
        Play a (quiet) game of Set.

        `return (tuple(integer, sets[]))`: Returns a tuple where the first item is the number of Sets discovered. The
            second item is the complete list of Sets.
        """
        self.board = self.deal(12)

        # Find sets and re-deal until we are out of cards.
        while len(self.deck) > 0:
            self.sets += self.find_sets(self.board)
            self.board += self.deal(3)

        # Find the very last set(s).
        self.sets += self.find_sets(self.board)

        # Return a tuple
        return (len(self.sets), self.sets)

    @staticmethod
    def display_cards(cards):  # pragma: no cover
        """
        Accepts an array of cards, and renders them for humans in a table to `stdout`.

        `cards (cards[])`: A list (i.e., array) of objects representing cards.

        `return (void)`
        """

        table = PrettyTable(["Number", "Color", "Shape", "Shading"])

        for card in cards:
            table.add_row([card["number"], card["color"], card["shape"], card["shading"]])

        print(table)

    @staticmethod
    def is_a_set(card1, card2, card3):
        """
        Determines whether a group of 3 cards is a _set_ or not.

        `card1 (card)`: A card object to compare against other card objects.

        `card2 (card)`: A card object to compare against other card objects.

        `card3 (card)`: A card object to compare against other card objects.

        `return (boolean)`: Whether or not the given cards represent a _Set_. A value of `True` means that the group is
            a set. A value of `False` means that the group is _not_ a set.
        """

        for attribute in ["color", "shape", "shading", "number"]:
            if (SetGame.__all_unique([
                    card1[attribute],
                    card2[attribute],
                    card3[attribute],
                ]) is False

                    and SetGame.__all_same([
                        card1[attribute],
                        card2[attribute],
                        card3[attribute],
                    ]) is False):

                return False

        # Did we actually make it all the way here?
        return True

    @staticmethod
    def find_sets(board):
        """
        Given a _Board_ of cards, determines whether or not it contains a _Set_.

        `board (cards[])`: A list (i.e., array) of Cards that are on the Board.

        `return (sets[])`: A list (i.e., array) of Sets. Each Set contains 3 Cards.
        """

        sets = []

        # Calculate the initial set of combinations.
        combinations = itertools.combinations(six.moves.range(len(board)), 3)

        # Run until we explicitly break.
        while True:

            # Grab the combination.
            combination = next(combinations, None)

            # As long as we didn't get a `None` back...
            while combination is not None:

                # Check to see if the three cards we got back for this combination are a Set.
                if SetGame.is_a_set(board[combination[0]], board[combination[1]], board[combination[2]]) is True:

                    # If so, save them.
                    sets.append([board[combination[0]], board[combination[1]], board[combination[2]]])

                    # After we save the Set, remove the cards from the Board.
                    # Python list indexes collapse automatically, so remove from the end first.
                    del board[combination[2]]
                    del board[combination[1]]
                    del board[combination[0]]

                    # This means that we now need to recalculate the Board, and start our loop over again.
                    combinations = itertools.combinations(six.moves.range(len(board)), 3)
                    break

                else:
                    # Move on to the next combination in the list.
                    combination = next(combinations, None)
                    continue

            # If we have reached the end of the list of combinations, quit.
            if combination is None:
                break

        # Return all matching sets.
        return sets

    @staticmethod
    def __all_unique(arr):
        """
        Determines whether or not a `List` of values are all unique.

        `arr (scalar[])`: A list (i.e., array) of scalar values to compare.

        `return (boolean)`: Whether or not a `List` of values are all different. A value of `True` means that the values
            are all unique. A value of `False` means that the values are not all unique.
        """

        return len(set(arr)) == len(arr)

    @staticmethod
    def __all_same(arr):
        """
        Determines whether or not a `List` of values are all identical.

        `arr (scalar[])`: A list (i.e., array) of scalar values to compare.

        `return (boolean)`: Whether or not a `List` of values are all identical. A value of `True` means that the values
            are all identical. A value of `False` means that the values are not all identical.
        """

        return len(set(arr)) == 1

    @staticmethod
    def plural(count, singular, plural):
        """
        Determines whether a response should be singular or plural, depending on the number of items being referenced.

        `count (integer)`: The number of items to adjust language for.

        `singular (string)`: The singular version of the phrasing.

        `plural (string)`: The plural version of the phrasing.

        `return (string)`: A properly-formatted string.
        """

        return "{count} {word}".format(
            count=count,
            word=singular
        ) if count == 1 else "{count} {word}".format(
            count=count,
            word=plural
        )

# ------------------------------------------------------------------------------


def main():  # pragma: no cover
    """
    This function is run when the script is executed from the command-line.
    """

    # Available CLI flags.
    parser = argparse.ArgumentParser(
        description="Play a game of Set.",
    )

    parser.add_argument(
        "-q", "--quiet",
        dest="quiet",
        action="store_true",
        help="By default, the game will play in chatty, interactive mode. "
        "This will enable a quieter, results-only mode.")

    parser.set_defaults(quiet=False)
    flags = parser.parse_args()
    game = SetGame()

    if flags.quiet:
        discovered, sets = game.play_quiet()
        print("You discovered {quantity}.".format(
            quantity=SetGame.plural(discovered, "set", "sets")
        ))

        for i, sset in enumerate(sets):
            print()
            print("Set #{index}".format(index=(i + 1)))
            SetGame.display_cards(sset)

    else:
        game.play()


if __name__ == "__main__":  # pragma: no cover
    main()

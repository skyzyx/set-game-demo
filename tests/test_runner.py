#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
A simple demo of the game of "Set".

Copyright (c) 2016 [Ryan Parman](https://github.com/skyzyx).

<http://opensource.org/licenses/Apache2.0>
"""

from __future__ import print_function
import unittest
import nose2
from set_game_demo import SetGame
from set_game_demo import SimpleNamespace

class Test(unittest.TestCase):
    """Unit tests for the set_game_demo.SetGame class."""

    def setUp(self):
        """Instantiate the class."""
        self.game = SetGame()

    # --------------------------------------------------------------------------
    # Properties

    def test_colors(self):
        self.assertTrue("red" in self.game.colors)
        self.assertTrue("green" in self.game.colors)
        self.assertTrue("purple" in self.game.colors)

        self.assertFalse("blue" in self.game.colors)
        self.assertFalse("fuschia" in self.game.colors)
        self.assertFalse("yellow" in self.game.colors)

    def test_shapes(self):
        self.assertTrue("diamond" in self.game.shapes)
        self.assertTrue("squiggle" in self.game.shapes)
        self.assertTrue("oval" in self.game.shapes)

        self.assertFalse("hearts" in self.game.shapes)
        self.assertFalse("clubs" in self.game.shapes)
        self.assertFalse("spades" in self.game.shapes)

    def test_shadings(self):
        self.assertTrue("solid" in self.game.shadings)
        self.assertTrue("empty" in self.game.shadings)
        self.assertTrue("striped" in self.game.shadings)

        self.assertFalse("spotted" in self.game.shadings)
        self.assertFalse("dotted" in self.game.shadings)
        self.assertFalse("criss-cross" in self.game.shadings)

    def test_numbers(self):
        self.assertTrue("one" in self.game.numbers)
        self.assertTrue("two" in self.game.numbers)
        self.assertTrue("three" in self.game.numbers)

        self.assertFalse("pi" in self.game.numbers)
        self.assertFalse("four" in self.game.numbers)
        self.assertFalse("five" in self.game.numbers)

    def test_deck(self):
        self.assertEqual(81, len(self.game.deck)) # Should be 3^4 (not 4^3)

    # --------------------------------------------------------------------------
    # Dealing

    def test_deal(self):
        self.assertEqual(3, len(self.game.deal(3)))
        self.assertEqual(6, len(self.game.deal(6)))
        self.assertEqual(12, len(self.game.deal(12)))
        self.assertEqual(12, len(self.game.deal()))
        # helper.assertRaises(IndexError, self.game.deal(48)) # Not quite working. 81 - 3 - 6 - 12 - 12 = 48

    # --------------------------------------------------------------------------
    # Utilities

    def test_all_unique(self):
        self.assertTrue(self.game._SetGame__all_unique(["red", "green", "purple"]))
        self.assertTrue(self.game._SetGame__all_unique(["diamond", "squiggle", "oval"]))
        self.assertTrue(self.game._SetGame__all_unique(["solid", "empty", "striped"]))
        self.assertTrue(self.game._SetGame__all_unique(["one", "two", "three"]))

        self.assertFalse(self.game._SetGame__all_unique(["red", "green", "green"]))
        self.assertFalse(self.game._SetGame__all_unique(["diamond", "squiggle", "squiggle"]))
        self.assertFalse(self.game._SetGame__all_unique(["solid", "empty", "empty"]))
        self.assertFalse(self.game._SetGame__all_unique(["one", "two", "two"]))

        self.assertFalse(self.game._SetGame__all_unique(["green", "green", "green"]))
        self.assertFalse(self.game._SetGame__all_unique(["squiggle", "squiggle", "squiggle"]))
        self.assertFalse(self.game._SetGame__all_unique(["empty", "empty", "empty"]))
        self.assertFalse(self.game._SetGame__all_unique(["two", "two", "two"]))

    def test_all_same(self):
        self.assertFalse(self.game._SetGame__all_same(["red", "green", "purple"]))
        self.assertFalse(self.game._SetGame__all_same(["diamond", "squiggle", "oval"]))
        self.assertFalse(self.game._SetGame__all_same(["solid", "empty", "striped"]))
        self.assertFalse(self.game._SetGame__all_same(["one", "two", "three"]))

        self.assertFalse(self.game._SetGame__all_same(["red", "green", "green"]))
        self.assertFalse(self.game._SetGame__all_same(["diamond", "squiggle", "squiggle"]))
        self.assertFalse(self.game._SetGame__all_same(["solid", "empty", "empty"]))
        self.assertFalse(self.game._SetGame__all_same(["one", "two", "two"]))

        self.assertTrue(self.game._SetGame__all_same(["green", "green", "green"]))
        self.assertTrue(self.game._SetGame__all_same(["squiggle", "squiggle", "squiggle"]))
        self.assertTrue(self.game._SetGame__all_same(["empty", "empty", "empty"]))
        self.assertTrue(self.game._SetGame__all_same(["two", "two", "two"]))

    def test_plural(self):
        self.assertEqual("0 things", self.game.plural(0, "thing", "things"))
        self.assertEqual("1 thing", self.game.plural(1, "thing", "things"))
        self.assertEqual("2 things", self.game.plural(2, "thing", "things"))

    # --------------------------------------------------------------------------
    # Set-detection

    def test_is_a_set1(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "red"
        card3.color = "red"

        card1.shape = "diamond"
        card2.shape = "diamond"
        card3.shape = "diamond"

        card1.shading = "solid"
        card2.shading = "solid"
        card3.shading = "solid"

        card1.number = "one"
        card2.number = "one"
        card3.number = "one"

        self.assertTrue(self.game.is_a_set(card1, card2, card3))

    def test_is_a_set2(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "green"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "diamond"
        card3.shape = "diamond"

        card1.shading = "solid"
        card2.shading = "solid"
        card3.shading = "solid"

        card1.number = "one"
        card2.number = "one"
        card3.number = "one"

        self.assertTrue(self.game.is_a_set(card1, card2, card3))

    def test_is_a_set3(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "green"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "squiggle"
        card3.shape = "oval"

        card1.shading = "solid"
        card2.shading = "solid"
        card3.shading = "solid"

        card1.number = "one"
        card2.number = "one"
        card3.number = "one"

        self.assertTrue(self.game.is_a_set(card1, card2, card3))

    def test_is_a_set4(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "green"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "squiggle"
        card3.shape = "oval"

        card1.shading = "solid"
        card2.shading = "empty"
        card3.shading = "striped"

        card1.number = "one"
        card2.number = "one"
        card3.number = "one"

        self.assertTrue(self.game.is_a_set(card1, card2, card3))

    def test_is_a_set5(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "green"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "squiggle"
        card3.shape = "oval"

        card1.shading = "solid"
        card2.shading = "empty"
        card3.shading = "striped"

        card1.number = "one"
        card2.number = "two"
        card3.number = "three"

        self.assertTrue(self.game.is_a_set(card1, card2, card3))

    def test_is_not_a_set1(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "red"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "squiggle"
        card3.shape = "oval"

        card1.shading = "solid"
        card2.shading = "empty"
        card3.shading = "striped"

        card1.number = "one"
        card2.number = "two"
        card3.number = "three"

        self.assertFalse(self.game.is_a_set(card1, card2, card3))

    def test_is_not_a_set2(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "red"
        card3.color = "red"

        card1.shape = "diamond"
        card2.shape = "diamond"
        card3.shape = "squiggle"

        card1.shading = "solid"
        card2.shading = "empty"
        card3.shading = "striped"

        card1.number = "one"
        card2.number = "two"
        card3.number = "three"

        self.assertFalse(self.game.is_a_set(card1, card2, card3))

    def test_is_not_a_set3(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "red"
        card3.color = "red"

        card1.shape = "diamond"
        card2.shape = "diamond"
        card3.shape = "diamond"

        card1.shading = "solid"
        card2.shading = "solid"
        card3.shading = "empty"

        card1.number = "one"
        card2.number = "two"
        card3.number = "three"

        self.assertFalse(self.game.is_a_set(card1, card2, card3))

    def test_is_not_a_set4(self):
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "red"
        card3.color = "red"

        card1.shape = "diamond"
        card2.shape = "diamond"
        card3.shape = "diamond"

        card1.shading = "solid"
        card2.shading = "solid"
        card3.shading = "solid"

        card1.number = "one"
        card2.number = "one"
        card3.number = "three"

        self.assertFalse(self.game.is_a_set(card1, card2, card3))

    # --------------------------------------------------------------------------
    # Finding sets

    def test_find_sets(self):

        # Cards which are a Set.
        card1 = SimpleNamespace()
        card2 = SimpleNamespace()
        card3 = SimpleNamespace()

        card1.color = "red"
        card2.color = "green"
        card3.color = "purple"

        card1.shape = "diamond"
        card2.shape = "squiggle"
        card3.shape = "oval"

        card1.shading = "solid"
        card2.shading = "empty"
        card3.shading = "striped"

        card1.number = "one"
        card2.number = "two"
        card3.number = "three"

        # Cards which are NOT a Set.
        card4 = SimpleNamespace()
        card5 = SimpleNamespace()
        card6 = SimpleNamespace()

        card4.color = "red"
        card5.color = "red"
        card6.color = "red"

        card4.shape = "diamond"
        card5.shape = "diamond"
        card6.shape = "diamond"

        card4.shading = "solid"
        card5.shading = "solid"
        card6.shading = "solid"

        card4.number = "one"
        card5.number = "one"
        card6.number = "three"

        # Find the Sets.
        board = [card4, card5, card6, card1, card2, card3]
        sets = SetGame.find_sets(board)

        self.assertEqual(1, len(sets))  # Find 1 Set.
        self.assertEqual(3, len(board)) # Number of cards remaining on the Board.

    def test_play_game(self):
        discovered, _ = self.game.play_quiet()
        self.assertTrue(discovered > 20 or discovered < 29)

# ------------------------------------------------------------------------------

if __name__ == '__main__':
    nose2.main()

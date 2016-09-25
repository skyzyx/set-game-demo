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
from nose2.tools.such import helper
from set_game_demo import SetGame

class Test(unittest.TestCase):
    """Unit tests for the set_game_demo.SetGame class."""

    def setUp(self):
        """Instantiate the class."""
        self.set = SetGame()

    def test_colors(self):
        self.assertEqual(True, "red" in self.set.colors)
        self.assertEqual(True, "green" in self.set.colors)
        self.assertEqual(True, "purple" in self.set.colors)
        self.assertEqual(False, "blue" in self.set.colors)
        self.assertEqual(False, "fuschia" in self.set.colors)
        self.assertEqual(False, "yellow" in self.set.colors)

    def test_shapes(self):
        self.assertEqual(True, "diamond" in self.set.shapes)
        self.assertEqual(True, "squiggle" in self.set.shapes)
        self.assertEqual(True, "oval" in self.set.shapes)
        self.assertEqual(False, "hearts" in self.set.shapes)
        self.assertEqual(False, "clubs" in self.set.shapes)
        self.assertEqual(False, "spades" in self.set.shapes)

    def test_shadings(self):
        self.assertEqual(True, "solid" in self.set.shadings)
        self.assertEqual(True, "empty" in self.set.shadings)
        self.assertEqual(True, "striped" in self.set.shadings)
        self.assertEqual(False, "spotted" in self.set.shadings)
        self.assertEqual(False, "dotted" in self.set.shadings)
        self.assertEqual(False, "criss-cross" in self.set.shadings)

    def test_numbers(self):
        self.assertEqual(True, "one" in self.set.numbers)
        self.assertEqual(True, "two" in self.set.numbers)
        self.assertEqual(True, "three" in self.set.numbers)
        self.assertEqual(False, "pi" in self.set.numbers)
        self.assertEqual(False, "four" in self.set.numbers)
        self.assertEqual(False, "five" in self.set.numbers)

    def test_deck(self):
        self.assertEqual(81, len(self.set.deck)) # Should be 3^4 (not 4^3)

    def test_deal(self):
        self.assertEqual(3, len(self.set.deal(3)))
        self.assertEqual(6, len(self.set.deal(6)))
        self.assertEqual(12, len(self.set.deal(12)))
        self.assertEqual(12, len(self.set.deal()))
        # helper.assertRaises(IndexError, self.set.deal(48)) # Not quite working. 81 - 3 - 6 - 12 - 12 = 48

if __name__ == '__main__':
    nose2.main()

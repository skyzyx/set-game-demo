# Set

## The Game
### Game Rules

"Set" is a card game where a group of players try to identify a "set" of cards from those placed face-up on a table.

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

## Requirements

* Python 2.7+, 3.5+
* Pip
* VirtualEnv is recommended, but not required

## Installation

```bash
# If you have VirtualEnv installed...
virtualenv .vendor
source .vendor/bin/activate

# Everybody
pip install -r requirements.txt
```

## Usage

```
# Application help
./set.py -h
```

## Problem Parameters


## Logic


## Known Issues


## Future Improvements

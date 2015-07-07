__author__ = 'Roland'
"""
Design a set of data structures to be used to implement a solitaire game such as Solitaire,
FreeCell, or Spider Solitaire. Provide the implementation either using your favorite
programming language or SQL. The implementation should provide the data, public
method interface and descriptions, but does not need to provide implementations of the
methods.
"""


#inheriting from object in accordance with PEPs 252 & 253; might not be necessary with Python 3
class Card(object):
    """
    A card representation that can be one of four suits (hearts,diamonds,clubs,spades) and 1-13 in value
    ie clubs,3 for a 3 of clubs, hearts,14 for ace of hearts
    """
    def __init__(self, suit, value):
        assert type(suit) is str and (value.isdigit() or value is str)

        suits = ['hearts', 'diamonds', 'clubs', 'spades']

        #ensure suit and values are appropriate to 'merica card games
        assert value in range(1, 14)
        assert suit in suits


class Deck(object):
    """
    A collection of cards. 52 cards consisting of all possible values of suit/value.
    """
    def __init__(self):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        values = range(1, 14)

        self.cards = []  # Create our deck
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))
        self.top = 0  # index for the deck

    def shuffle(self):
        # random(self.cards)
        pass

    def draw(self):
        drawn = self.cards[self.top]
        self.cards.remove(drawn)
        return drawn


class Game(object):
    """
    Implementation of the various rules governing whatever game is played.
    """
    def __init__(self):
        self.timelimit = 0  # value in case implementation sets a time limit


class Player(object):
    """
    A player that includes values such as score, time, etc.
    """
    def __init__(self):
        self.score = 0
        self.time = 0


class Scoreboard(object):
    """
    Record of high scores saved as a flat file
    """
    def __init__(self, file):
        self.scores = open(file, 'w')

    def newEntry(self, name, score):
        self.name = name
        self.score = score
        self.scores.write(self.name + ' : ' + self.score)
        pass

if __name__ == '__main__':
    testDeck = Deck

import random

class Card:
    def __init__(self, value):
        """
        Initialize the card with a value
        """
        self.value = value

class Deck:
    def __init__(self):
        """
        Initialize the deck with a list of shuffled cards
        """
        self.cards = [Card(i) for i in range(1, 101)]
        random.shuffle(self.cards)

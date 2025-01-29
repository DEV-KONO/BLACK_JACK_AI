import random
from BLACKJACK.card import card

symbols = ["Hearts", "Spades", "Diamonds", "Clubs"]
values = ["Ace", 2,3,4,5,6,7,8,9,10,"Jack", "Queen", "King"]


class deck:
    def __init__(self):
        self.current = []
        self.discarded = []
        for symbol in symbols:
            if symbol == "Hearts" or symbol == "Diamonds":
                for value in values:
                    self.current.append(card(symbol,"Red", value))
            else:
                for value in values:
                    self.current.append(card(symbol, "Black", value))
    def __str__(self):
        for i in self.current:
            return f"{i}"
        
    def shuffle(self):
        random.shuffle(self.current)
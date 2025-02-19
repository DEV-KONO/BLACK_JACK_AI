import random

class player:
    def __init__(self, behaviour):
        self.current_cards = []
        self.card_sum = 0
        self.behaviour = behaviour

    def play(self):
        if self.behaviour == "Noob":
            return random.choice(["H", "S"])
        
        elif self.behaviour == "Normal":
            if self.card_sum > 11:
                return "S"
            else:
                return "H"
        
        elif self.behaviour == "Intermediate":
            if self.card_sum <= 11:
                return "H"
            
            
        
    def count(self):
        self.card_sum = 0
        for i in self.current_cards:
            print(f"Player Cards: {i}")
            if type(i.value) == str and i.value != "Ace":
                self.card_sum += 10
            elif type(i.value) == str and i.value == "Ace":
                if self.card_sum + 11 >= 21:
                    self.card_sum += 1
                else:
                    self.card_sum += 11
            else:
                self.card_sum += i.value
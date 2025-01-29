from sympy import true


class player:
    def __init__(self):
        self.current_cards = []
        self.card_sum = 0

    #no actual use
    def Analize(self):
        if self.card_sum <= 11:
            return True
        else:
            return False
        
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
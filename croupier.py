from BLACKJACK.player import player

class croupier(player):
    
    def count(self):

        self.card_sum = 0

        for i in self.current_cards:
        
            if i.visible:
            
                print(f"Croupier Cards: {i}")

                if type(i.value) == str and i.value != "Ace":
                
                    self.card_sum += 10

                elif type(i.value) == str and i.value == "Ace":
                
                    if self.card_sum + 11 >= 21:
                    
                        self.card_sum += 1

                    else:
                    
                        self.card_sum += 11

                else:
                
                    self.card_sum += i.value

            else:
            
                print(f"Croupier Cards: Flipped")
    
    def flip(self):
        self.current_cards[0].visible = False

    def reveal(self):
        self.current_cards[0].visible = True
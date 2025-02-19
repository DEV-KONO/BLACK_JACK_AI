from croupier import croupier
from deck import deck
from player import player

Deck = deck()
Croupier = croupier()
Player_1 = player(behaviour="Noob")
end_game = False
hs_loop = True

def printsum():
    print(f"Player Sum: {Player_1.card_sum}; Croupier Sum: {Croupier.card_sum}")

def give_card_to(Player: player|croupier, Deck: deck):
    Player.current_cards.append(Deck.current.pop())

Deck.shuffle()

give_card_to(Croupier, Deck)
Croupier.flip()
give_card_to(Player_1, Deck)
give_card_to(Croupier, Deck)
give_card_to(Player_1, Deck)

Player_1.count()
Croupier.count()
printsum()
while hs_loop:
    Player_1_Choice = Player_1.play()
    print(f"Player 1 Hit/Stand (H/S): {Player_1_Choice}")
    if Player_1_Choice.lower() == "h":
        give_card_to(Player_1, Deck)
        Player_1.count()
    elif Player_1_Choice.lower() == "s":
        Player_1.count()
        hs_loop = False
    else:
        print("Not a valid choice!!")
        continue
    if Player_1.card_sum > 21:
        print("You LOST!!!")
        hs_loop = False
    elif Player_1.card_sum == 21:
        print("Black Jack!!!")
        break
    printsum()
hs_loop = True
Croupier.flip()
while hs_loop:
    Croupier.count()
    
    printsum()
    if Croupier.card_sum < 16:
        give_card_to(Croupier, Deck)
    else:
        hs_loop = False
    Croupier.count()
    printsum()
if (Player_1.card_sum > 21) or (Player_1.card_sum < Croupier.card_sum) and Croupier.card_sum <= 21:
    print("You LOST :(")
elif (Player_1.card_sum == 21 and Croupier.card_sum != Player_1.card_sum) or (Player_1.card_sum > Croupier.card_sum) or (Croupier.card_sum >21):
    print("You WON :)")
elif (Player_1.card_sum == Croupier.card_sum) or (Player_1.card_sum == Croupier.card_sum):
    print("Tie :| ")
from croupier import croupier
from deck import deck
from player import player

Deck = deck()
Croupier = croupier()
Player_1 = player()
end_game = False
hs_loop = True

def printsum():
    print(f"Player Sum: {Player_1.card_sum}; Croupier Sum: {Croupier.card_sum}")

for i in Deck.current:
    # print(i)
    pass

Deck.shuffle()

# print("\n\nPrinting shuffled deck:")

for i in Deck.current:
    # print(i)
    pass

while not end_game:
    Croupier.current_cards.append(Deck.current.pop())
    Croupier.flip()
    Player_1.current_cards.append(Deck.current.pop())
    Croupier.current_cards.append(Deck.current.pop())
    Player_1.current_cards.append(Deck.current.pop())
    
    Player_1.count()
    Croupier.count()

    printsum()

    while hs_loop:
        Player_1_Choice = input("Hit/Stand? (H/S): ")

        if Player_1_Choice.lower() == "h":
            Player_1.current_cards.append(Deck.current.pop())
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

        printsum()

    hs_loop = True

    Croupier.reveal()

    while hs_loop:
        Croupier.count()
        
        printsum()

        if Croupier.card_sum < 16:
            Croupier.current_cards.append(Deck.current.pop())
        else:
            hs_loop = False

        Croupier.count()

        printsum()

    if (Player_1.card_sum > 21) or (Player_1.card_sum < Croupier.card_sum):
        print("You LOST :(")
    elif (Player_1.card_sum == 21 and Croupier.card_sum != Player_1.card_sum) or (Player_1.card_sum > Croupier.card_sum):
        print("You WON :)")
    elif (Player_1.card_sum == Croupier.card_sum) or (Player_1.card_sum == Croupier.card_sum):
        print("Tie :| ")

    end_game = True
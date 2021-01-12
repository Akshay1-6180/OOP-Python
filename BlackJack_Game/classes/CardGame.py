from .Deck import Deck
from .Card import Card

class CardGame:

    INSTRUCTIONS = """\n | Welcome to our version of the Blackjack Game |
=================================================================================
The goal is to get as close to 21 as possible, without going over 21. 
Each card has a value and a suit. The values are added for the final result.

The game starts by dealing two cards to the player (you) and to the dealer.            
You are playing against the dealer. On each turn, you must choose if you
would like to take another card or stand to stop the game and see if you won.

The game ends if the total value of the player's hand goes over 21,
and if the total value of the hand is below 21, the game continues
until the player chooses to stand.

When the game ends or when the player chooses to stand,
the total value of each hand is calculated.  
The value that is closest to 21 without going over it wins the game.
If the total value is over 21, the player or dealer automatically lose the game.
=================================================================================
"""
    def __init__(self, deck, player, dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer
        self.start_game()

    def start_game(self):
        print(CardGame.INSTRUCTIONS)
        turn = 1

        self.deck.shuffle()
        self.player.draw(self.deck).draw(self.deck)
        self.dealer.draw(self.deck).draw(self.deck)

        while True:
            print(f"== Turn #{turn} ==")

            print("\n The dealers Hand is:")

            self.dealer.show_hand()

            print("your hand is:")

            self.player.show_hand()

            if self.player.get_hand_value() > 21:
                print("\n The total value of your hand is over 21")

                break
            elif self.player.get_hand_value() == 21:
                break
            
            choice = self.ask_choice()
            turn +=1

            if choice ==1:
                self.player.draw(self.deck)
            
            else:
                break
        player_hand = self.player.get_hand_value()
        print("\n Value - Your Hand:", player_hand)

        dealer_hand = self.dealer.get_hand_value()
        print("\n Value - Dealers Hand:", dealer_hand)

        print("\n The Dealer's Hand was:")
        self.dealer.show_hand(True)


        if player_hand > 21:
            print(f"\n You lose, {self.player.name} ")
        elif dealer_hand>21 or player_hand==21 or player_hand>dealer_hand:
            print(f"\n you win {self.player.name} ")
        elif player_hand < dealer_hand:
            print(f"\n Your lose {self.player.name} ")
        else:
            print("we have a tie")

    def ask_choice(self):
        print("\n What do you want to do")
        print("1 - Ask for another card")
        print("2 - Stand")
        choice = int(input("PLease enter your choice(1 or 2)"))
        if choice ==1 or choice == 2:
            return choice
        
        else:
            print("the value was not valid, going for stand")
            return 2
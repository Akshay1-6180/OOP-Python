from classes.Deck import Deck
from classes.Card import Card
from classes.Player import Player
from classes.CardGame import CardGame

# need 3 classes - card,deck,player
deck = Deck()
you = Player("Akshay")
dealer = Player("Dealer", True)

game = CardGame(deck, you, dealer)

import random
from . import card

class Deck:
    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,15):
                str_val = ""
                if i == 14:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( card.Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_cards(self):
        random.shuffle(self.cards)
        return self

    def player_hand(self):
        return self.cards[0:26]

    def show_player_hand(self):
        for card in self.player_hand():
            card.card_info()

    def computer_hand(self):
        return self.cards[26:52]

    def show_computer_hand(self):
        for card in self.computer_hand():
            card.card_info()

    def discard_stack(self):
        self.discards = []
        return self

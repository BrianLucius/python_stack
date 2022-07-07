from classes.deck import Deck
import random

bicycle = Deck()

bicycle.shuffle_cards()

bicycle.player_hand()
bicycle.computer_hand()

print("player")
bicycle.show_player_hand()
print("computer")
bicycle.show_computer_hand()


# bicycle.show_cards()  # deck


# player_hand.show_cards()

# print(player_hand)

# player_hand.card_info()

# player_hand = bicycle.cards[0:25]
# print(player_hand.card_info()

# bicycle.cards[0].card_info()


# mylist = ["apple", "banana", "cherry"]
# random.shuffle(mylist)

# print(mylist)


# random_number = Math.random(1..52)
# player_hand.append(self.cards[random_number])


# War
#     Real player vs computer
#     Split the deck in two
#     each player places a card from the top of the deck
#     Highest card (aces high) wins the "battle"
#     winner takes both cards for the round/battle, place on discard stack
#     Discard stack is re-shuffled when one player is out of cards
#     keep playing rounds until one player has all 52 cards 

# Randomize cards into two separate dictionaries (player_hand dict, computer_hand dict) (player_disc dict, computer_disc dict)
#     Player uses a keyboard input to place a card in the "playfield"
#     Computer place a card after player places a card
#     Compare the cards, winner adds both cards to their ownn discard stack
#     check each player to see if there or no cards left in their hand, 
#         if no cards in hand, shuffle your discard stack, this is new hand
#     repeat play until one players discard stack is empty
    
# class card_stack
#     instance player_hand
#     instance player_discard
#     instance computer_hand
#     instance computer_discard
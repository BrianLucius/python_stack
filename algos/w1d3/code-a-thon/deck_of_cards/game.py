from classes.deck import Deck

bicycle = Deck()

bicycle.shuffle_cards()

bicycle.player_hand()
bicycle.computer_hand()

player_discard_stack = bicycle.discard_stack()
computer_discard_stack = bicycle.discard_stack()

# print("\n***** player *****")
# bicycle.show_player_hand()
# bicycle.player_hand().pop(0)

# print("\n***** computer *****")
# bicycle.show_computer_hand()

print(" ******* THIS IS WAR!!! *******")
while len(bicycle.player_hand()) > 0 and len(bicycle.computer_hand()) > 0:
    player1 = input("Press enter to play a card!")

    print("Your card: ")
    bicycle.player_hand()[0].card_info()

    [print("The computer's card: ")]
    bicycle.computer_hand()[0].card_info()

    if bicycle.player_hand()[0].point_val > bicycle.computer_hand()[0].point_val:
        print("You win this round and take the cards!")
        player_discard_stack.discards.append(bicycle.player_hand()[0])
        player_discard_stack.discards.append(bicycle.computer_hand()[0])
        bicycle.player_hand().pop(0)
        bicycle.computer_hand().pop(0)
    elif bicycle.player_hand()[0].point_val < bicycle.computer_hand()[0].point_val:
        print("You lost this round. Computer takes the cards")
        computer_discard_stack.discards.append(bicycle.player_hand()[0])
        computer_discard_stack.discards.append(bicycle.computer_hand()[0])
        bicycle.player_hand().pop(0)
        bicycle.computer_hand().pop(0)



#

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
#     Compare the cards, winner adds both cards to their own discard stack
#     check each player to see if there or no cards left in their hand, 
#         if no cards in hand, shuffle your discard stack, this is new hand
#     repeat play until one players discard stack is empty
    
# class card_stack
#     instance player_hand
#     instance player_discard
#     instance computer_hand
#     instance computer_discard
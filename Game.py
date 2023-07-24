#-------------------------------------------------------------------------------
# Name:        Herbaceous draft for solo play
# Purpose:     logic for digital solo play (currently - text version only) of card game called "Herbaceous"
# Author:      aszku
# Created:     VII 2023 - ?
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# To do list:
# - add potting mechanics
# - improve the description of pots and the way game communicates with the player
# - modify code to include gui
#
#-------------------------------------------------------------------------------

import HerbsDeck
import sys

#-------------------------------------------------------------------------------

def MainGame():
    deck = HerbsDeck.CardsDeck()
    print("Deck created")
    turn = 1 # turn number
    GameNotEnded = True
    priv_garden = [] # contains cards in the private garden
    com_garden = [] # contains cards in the community garden
    discard = [] # contains cards in the discard pile
    available_pots = ["g", "l", "w", "s"]
    #Glass Jar (any 3 herbs. the only place you can place special herbs), Large Pot (1 type of identical herbs), Wooden Planter (different herbs), Small Pots (pair of identical herbs)
    x = "" # variable helper
    def wants_out(x_input):
        if x_input == "x" or x_input == "X":
            x = input("Are you sure you want to leave the game? [y/n] ... ")
            if x == "y" or x == "Y":
                sys.exit("You decided to quit the game.")
            elif x == "x" or x == "X":
                wants_out(x) # hi recurrence
    def show_state_of_the_game():
        print("\nCards currently in the Private Garden: ", priv_garden)
        print("Cards currently in the Community Garden: ", com_garden)
        if len(com_garden) == 5:
            print("Community Garden has too many cards! All its cards are discarded: ", com_garden)
            discard.extend(com_garden)
            com_garden.clear()
            print("Cards currently in the Community Garden: ", com_garden)
        print("Cards currently in the Discard Pile: ", discard)
        print("Pots") #dodaj summary for pots
    while GameNotEnded: # when game is ongoing
        i = 0 # number of cards being drawn during a turn
        chosen_places = []
        print(f"\n\n #-#-#-# Turn {turn} #-#-#-# ")

        if i == 0 and available_pots:
            show_state_of_the_game()
            x = input("# Do you wanna repot any cards? [y/n] ... ")
            wants_out(x)
            if x == "y" or x == "Y":
                print(f"You chose to pot. There are 4 containers in the game, {len(available_pots)} available. \n \n \
                g - Glass Jar - \n \
                l - Large Pot - \n \
                w - Wooden Planter - \n \
                s - Small Pots \n ") # perform here "switch cases" = match case + descriptions?
                available_pots_txt = "" # add loop to have a text for next line
                chosen_pot = input(f"Potting to which container? [g/l/w/s/c] (press c for cancel potting) ... ") # improve the desciption, use available_pots_txt
                wants_out(chosen_pot)
                if chosen_pot == "c":
                    print("Not repotting.")
                else:
                    print(f"Potting to chosen container: {chosen_pot}") # chosen_pot can be later replaced by dict? (g-Glass jar - shortcut key, name value) or object (g.name = glass jar, g.action = ...)
            else:
                print("Not repotting.")
        for i in (0, 1, 2):
            def decision_go(decision):
                wants_out(decision)
                chosen_places.append(decision)
                if decision == "d":
                    discard.append(drawn_card.herb_name)
                elif decision == "c":
                    com_garden.append(drawn_card.herb_name)
                elif decision == "p":
                    priv_garden.append(drawn_card.herb_name)
            show_state_of_the_game()
            drawn_card = deck.draw_card()
            print(f" ## Drawn card: {drawn_card.herb_name}. ", end="\n")
            if i == 2:
                for i in ("d", "c", "p"):
                    if i not in chosen_places: decision = i
                else:
                    print(f"It is the last card in the turn, so it goes automatically to not chosen place: ... {decision}")
                    decision_go(decision)
            else:
                decision_ok = False
                while not decision_ok:
                    decision = input("What do you want to do with this card? [d/c/p] \n(press d for discard, c for putting in community garden, p for putting in private garden)  ... ")
                    wants_out(decision)
                    if decision not in ("d", "c", "p"):
                        print("Please enter correct input. ", end="\n")
                    elif decision in chosen_places:
                        print("You cannot choose this option now, you've already added a card to this place in this turn. ", end="\n")
                    else:
                        decision_ok = True
                        decision_go(decision)
        chosen_places.clear()
        if turn == 11: # warning jak zostaly ostatnie trzy karty w decku
            print("=== Beware, this will be the final turn! ===")
        if turn == 12: # gdy nie ma juz kart w decku
            GameNotEnded = False
        if not available_pots:
            break
        turn += 1
    else:
        # last pot usage after cards ended
        print("placeholder: here will be final use of pot in case deck has ended")
    # here to add final scoring and summary
    print("placeholder: here will be final scoring calculation and summary")

#---------

print("Hello")
MainGame()


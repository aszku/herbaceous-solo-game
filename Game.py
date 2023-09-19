#-------------------------------------------------------------------------------
# Name:        Herbaceous draft for solo play
# Purpose:     logic for digital solo play (text version only)
#              of a card game called "Herbaceous"
#              wip - v.0.03
# Author:      aszku
# Created:     VII 2023 - ?
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# To do list:
    # - pots other than g: remove special herbs from helper at start of repotting
    # - w pot: finish adding including the check if the card type wasn't chosen earlier
    # generalize choosing card and possibly add personalized Exception classes
# - add potting mechanics
# - add stripping each input (slice [:2]) # i have no idea what I meant here previously
# - improve the description of pots and the way game communicates with the player
# - modify code to include gui
#
#-------------------------------------------------------------------------------

import HerbsDeck
import sys

#-------------------------------------------------------------------------------

def MainGame():
    print("Welcome to the game. (Press x during any choice to quit the game.)")
    deck = HerbsDeck.CardsDeck()
    print("Deck created")
    turn = 1 # turn number
    GameNotEnded = True
    priv_garden = [] # contains cards in the private garden
    com_garden = [] # contains cards in the community garden
    discard = [] # contains cards in the discard pile
    available_pots = ["g", "l", "w", "s"]
    choice_dict = dict(g = "Glass Jar", l = "Large Pot", w = "Wooden Planter", s = "Small Pot")
    filled_g = [] # for herbs in the pot
    filled_l = [] # for herbs in the pot
    filled_w = [] # for herbs in the pot
    filled_s = [] # for herbs in the pot
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
            print("Community Garden has too many cards! All its cards are discarded!")
            discard.extend(com_garden)
            com_garden.clear()
            print("Cards currently in the Community Garden: ", com_garden)
        print("Cards currently in the Discard Pile: ", discard)
        pots_available_dict = [choice_dict[n] for n in available_pots]
        print(f"Pots avalaible: {pots_available_dict} ")         # opcjonalnie, dodaj summary co zawieraja pots used

    def choose_card(available_cards_list, chosen_already): #to be generalized later...
        pass

    def repot_g(helper, filled_g):  #
        print(f"Choose 3 cards to put in the Glass Jar from: {helper}")
        chosen_to_pot = []
        for i in [1,2,3]:
            while True:
                print(f"chosen_to_pot = {chosen_to_pot}")
                chosen_card_index = input(f"Choose card no {i}: ... ")
                wants_out(chosen_card_index)
                try:
                    chosen_card_index = int(chosen_card_index)
                    if chosen_card_index > len(helper): raise IndexError("")
                    if chosen_card_index not in [int(index) for [index,value,gardentype] in helper]: raise ValueError("")
                    if chosen_card_index in chosen_to_pot: raise Exception("")
                except IndexError:
                    print(f"The card number is too high! ")
                except ValueError:
                    print(f"Incorrect input. Please enter viable card number! ") # print("Incorrect input. Please enter index for available cards.", end="\n")
                except:
                    print(f"You've already chosen this card! ")
                else:
                    print(f"Chosen: {helper[chosen_card_index-1]}. ", end="")
                    chosen_to_pot.append(chosen_card_index)
                    print(f"chosen_to_pot after adding = {chosen_to_pot}")
                    filled_g += [helper[chosen_card_index-1][1]]
                    if helper[chosen_card_index-1][2] == "(private)":
                        priv_garden.remove(helper[chosen_card_index-1][1])
                    else:
                        com_garden.remove(helper[chosen_card_index-1][1])
                    break
        else:
            print(f"", end="\n")
        print(f"These 3 cards were put in the Glass Jar: {filled_g}")
        # add removing these cards... and filling new dict?

    def repot_l(helper, filled_l):  #
        print("Here will be repotting to l (placeholder)")
        print(f"Choose number for card type to move to Large Pot: {helper}")
        chosen_to_pot = []
        while True:
            chosen_card_index = input(f"Choose card number: ... ")
            wants_out(chosen_card_index)
            try:
                chosen_card_index = int(chosen_card_index)
                if chosen_card_index > len(helper): raise IndexError("")
                if chosen_card_index not in [int(index) for [index,value,gardentype] in helper]: raise ValueError("")
                if chosen_card_index in chosen_to_pot: raise Exception("")
            except IndexError:
                print(f"The card number is too high! ")
            except ValueError:
                print(f"Incorrect input. Please enter viable card number! ") # print("Incorrect input. Please enter index for available cards.", end="\n")
            except:
                print(f"You've already chosen this card! ")
            else:
                print(f"Chosen: {helper[chosen_card_index-1]}. ", end="")
                chosen_to_pot.append(chosen_card_index)
                print(f"chosen_to_pot after adding = {chosen_to_pot}")
                filled_l += [helper[chosen_card_index-1][1]]
                if helper[chosen_card_index-1][2] == "(private)":
                    priv_garden.remove(helper[chosen_card_index-1][1])
                else:
                    com_garden.remove(helper[chosen_card_index-1][1])
                automatic = input("Do you want to fill the containter with all available cards of this type (y) or manually choose other cards (n)?")
                wants_out(automatic)
                if automatic == "y" or automatic == "Y":
                    counter_of_same_cards = sum([(value==helper[chosen_card_index-1][1]) for [index,value,gardentype] in helper])
                    filled_l += (counter_of_same_cards-1) * filled_l
                    for h in helper:
                        if h[1] == helper[chosen_card_index-1][1] and h != helper[chosen_card_index-1]:
                                if h[2] == "(private)":
                                    priv_garden.remove(h[1])
                                else:
                                    com_garden.remove(h[1])
                elif automatic == "n" or automatic == "N":
                    for h in helper:
                        if h[1] == helper[chosen_card_index-1][1] and h != helper[chosen_card_index-1]:
                            xyz = input(f"Card {h[0]} from {h[2][1:-1]} garden - do you want to add it to the pot?")
                            wants_out(xyz)
                            if xyz == "y" or xyz == "Y":
                                filled_l += [h[1]]
                                if h[2] == "(private)":
                                    priv_garden.remove(h[1])
                                else:
                                    com_garden.remove(h[1])
                    print("No more cards of this type!")
                break
        print(f"Repotting finished. These cards were put in the Large Pot: {filled_l}")



    def repot_w(helper, filled_w):  # wip
        already_chosen_types = []
        chosen_to_pot = []
        helper.insert(0, [0, "No more cards to be added!", "n/a"])
        while True:
            chosen_card_index = input(f"Choose number for card to move to Wooden Planter: {helper}")
            wants_out(chosen_card_index)
            try:
                chosen_card_index = int(chosen_card_index)
                if chosen_card_index > len(helper): raise IndexError("")
                if chosen_card_index not in [int(index) for [index,value,gardentype] in helper]: raise ValueError("")
                if chosen_card_index in chosen_to_pot: raise Exception("")
            except IndexError:
                print(f"The card number is too high! ")
            except ValueError:
                print(f"Incorrect input. Please enter viable card number! ") # print("Incorrect input. Please enter index for available cards.", end="\n")
            except:
                print(f"You've already chosen this card! ")
            else:
                print(f"Chosen: {helper[chosen_card_index-1]}. ", end="")
                chosen_to_pot.append(chosen_card_index)
                print(f"chosen_to_pot after adding = {chosen_to_pot}")
                filled_w += [helper[chosen_card_index-1][1]]
                if helper[chosen_card_index-1][2] == "(private)":
                    priv_garden.remove(helper[chosen_card_index-1][1])
                else:
                    com_garden.remove(helper[chosen_card_index-1][1])
                if len(chosen_to_pot) < 8: #what's the max size of this container? 8? or less?
                    xyz = input("Do you want to add another card (of different type than already in the planter)? (y/n)")
                    wants_out(xyz)
                    if xyz == "y" or xyz == "Y":
                        pass # do some recurrency here?
                    elif xyz == "n" or xyz == "N":
                        break
                else:
                    break
        print("Repotting finished. These cards were put in the Wooden Planter: {filled_w}")

    def repot_s(helper, filled_s):  # todo
        print("Here will be repotting to s (placeholder)")

    def learn_about_pots():
        print(f"There are 4 containers in the game. If you use a container, it is filled and can't be used again. \n \n \
        g - Glass Jar - You can put there any 3 Herbs. It is the only place you can put Special Herbs in. \n \
        l - Large Pot - You can fill it with one type of Herbs. \n \
        w - Wooden Planter - You can fill it with different Herbs (no duplicate Herbs allowed!) \n \
        s - Small Pot - You can fill it with pairs of identical Herbs, example: two Bays, two Tarragons, two Saffrons would make 3 pairs. You can use several pairs of a single Herb, for example four Lavender cards make up two pairs.\n ")

    def rules():    # add rules, then add "In the beginning of each turn, you can do repotting from the cards gathered in Private Garden and Community Garden. " i learn_about_pots()
        pass

    while GameNotEnded: # when game is ongoing
        i = 0 # number of cards being drawn during a turn
        chosen_places = []
        print(f"\n\n #-#-#-# Turn {turn} #-#-#-# ")

        if (turn != 1) and (i == 0) and available_pots: #available_pots check not needed - if its false, the game ends
            show_state_of_the_game()
            x = input("# Do you wanna repot any cards? [y/n/l] (press l to learn more) ... ")
            wants_out(x)
            if x == "l":
                learn_about_pots()
                x = input("# Do you wanna repot any cards? [y/n] ... ")
            if x == "y" or x == "Y": #this should be moved to separate function, and reuse learn_about_pots() somehow
                print(f"You chose to pot. There are 4 containers in the game, {len(available_pots)} available: {available_pots}. If you use a container, it is filled and can't be used again. \n \n \
                g - Glass Jar - You can put there any 3 Herbs. It is the only place you can put Special Herbs. \n \
                l - Large Pot - You can fill it with one type of Herbs. \n \
                w - Wooden Planter - You can fill it with different Herbs (no duplicate Herbs allowed!) \n \
                s - Small Pot - You can fill it with pairs of identical Herbs, example: two Bays, two Tarragons, two Saffrons would make 3 pairs. You can use several pairs of a single Herb, for example four Lavender cards make up two pairs.\n ") # +descriptions?
                available_pots_txt = ""
                for index in available_pots:
                    available_pots_txt = available_pots_txt + index + "/"
                while True:
                    chosen_pot = input(f"Repot to which container? [{available_pots_txt}c] (press c for cancel repotting) ... ")
                    if chosen_pot not in list(available_pots+["c"]+["x"]):
                        print("Please provide correct input.")
                    else:
                        wants_out(chosen_pot)
                        if chosen_pot == "c":
                            print("Repotting cancelled.")
                        else:
                            choice = choice_dict[chosen_pot]
                            print(f"Repotting to chosen container: {choice}")
                            helper = []
                            for index, value in enumerate(com_garden):
                                a = [index+1, value, "(community)"]
                                helper.append(a)
                            for index, value in enumerate(priv_garden):
                                a = [len(helper)+1, value, "(private)"]
                                helper.append(a)
                            print("Cards to choose from during repotting: ",helper)
##                            sys.exit("Debug/test exit.") # for testing purpose
                            if chosen_pot == "g":
                                repot_g(helper, filled_g)
                            # add here action for various potting
                            if chosen_pot == "s":
                                pass
                            if chosen_pot == "w":
                                repot_w(helper, filled_w)
                            if chosen_pot == "l":
                                repot_l(helper, filled_l)
                            available_pots.remove(chosen_pot)
                            break
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

MainGame()


#-------------------------------------------------------------------------------
# Name:        Herbaceous deck for solo play
# Purpose:     preparing classes and functions to use during a solo digital play of card game called "Herbaceous"
#              later to be used in game module
# Author:      aszku
# Created:     VII 2023 - ?
#-------------------------------------------------------------------------------

import random

class CardsDeck:
    current_deck = []

    def __init__(self):
        current_deck = self.current_deck
        # prepare list of 72 cards of herbs and special herbs
        for i in range(1,73):
            if i in range(1,9): herb_name = "Saffron"
            if i in range(10,18): herb_name = "Rosemary"
            if i in range(19,27): herb_name = "Dill"
            if i in range(28,36): herb_name = "Sage"
            if i in range(37,45): herb_name = "Lavender"
            if i in range(46,54): herb_name = "Bay"
            if i in range(55,63): herb_name = "Taragon"
            if i in range(64,66): herb_name = "Mint (1)"  # special herb
            if i in range(67,69): herb_name = "Chive (2)" # special herb
            if i in range(70,72): herb_name = "Thyme (3)"  # special herb
            card_name = f"card_{i}"
            current_deck += [Card(card_name, herb_name)]

        # shuffle them and remove half of the deck
        random.shuffle(current_deck)
        for i in range(36):
            current_deck.pop()

    def testing_show_deck(self):
        current_deck = self.current_deck
        print(f"current_deck len = {len(current_deck)}")
        print(current_deck)

    def draw_card(self):
        current_deck = self.current_deck
        drawn_card = current_deck.pop()
        return drawn_card

class Card:
    def __init__(self, card_name, herb_name):
        self.herb_name = herb_name
        self.card_name = card_name

##    def __str__(self):
##        return f"{self.card_name}({self.herb_name})"

    def __repr__(self):
        return f"{self.card_name}({self.herb_name})"

class PlantContainer:
    def __init__(self, container_type):
        pass

class CardsSpace:
    def __init__(self, field_name):
        # CommunityGarden, PrivateGarden, DiscardPile, CurrentTurnCard?, CurrentChoice?, HerbBisquitMarker?
        pass



"""
The game solo:
    remove random 36 cards from the deck
    1st card is used as a start of the Discard Pile
    2 cards are placed to the Community Garden
    3 cards are placed in Private Garden
    In the turn, player:
        can firstly repot herbs (take any number of cards in Gardens and place them in unused pot)
            if a player managed to score in the glass jar all three types of cards with points (1,2,3), he gets Herb Bisquit bonus *special herbs may be placed only in Glass Jar Container
            pots type: Glass Jar (any 3 herbs. the only place you can place special herbs), Large Pot (1 type of identical herbs), Wooden Planter (different herbs), Small Pots (pair of identical herbs)
        has to draw 3 new cards:
            drawing one at a time, immediately as it is shown, player decides where the card goes (1 card must be placed in Discard Pile, 1 card in Private Garden, 1 card in Community Garden
            if at any moment CommG consists of 5 cards, you need to discard them all
        game ends when there is no pots left or deck as ended. if deck has ended, player may additionally perform repotting once.
cards: https://boardgamegeek.com/image/2948992/herbaceous
cards types: saffron, dill, sage, rosemary, lavender, bay, taragon, mint 1, chive 2, thyme 3
9x each normal type card and 3x each special type card

points:
    < 37 Fledgling Grower
    37-41 Beginning Planter
    42-46 Clever Cultivator
    47-51 Talented Gardener
    52-56 Professional Herbalist
    57+ True Green Thumb Harvester

"""


def main():
    print("Performing testing...")
    tested_deck = CardsDeck()
##    print("Deck at start pre shuffle")
##    tested_deck.testing_show_deck()
##    print("Deck after shuffle")
##    tested_deck.testing_show_deck()
    print("Deck after shuffle & cut in half")
    tested_deck.testing_show_deck()
    drawn = tested_deck.draw_card()
    print(f"Deck after drawn {drawn}:")
    tested_deck.testing_show_deck()

if __name__ == '__main__':
    main()
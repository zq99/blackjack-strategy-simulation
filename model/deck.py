import random
from common.util import full_range
from model.card import Suit,create_ace_card,create_royal_card,create_number_card


def create_game_deck(number_of_decks=1):
    # this is main method for creation
    game_deck = GameDeck()
    for _ in full_range(1, number_of_decks):
        deck = __create_single_deck()
        game_deck.add_deck(deck)
    return game_deck


def __create_single_deck():
    deck = __Deck()
    suits = [Suit.Diamonds, Suit.Hearts, Suit.Clubs, Suit.Spade]

    # populate the number cards for all suits (36 in total)
    for n in full_range(1, 9):
        for s in suits:
            card = create_number_card(n, s)
            deck.add_card(card)

    # 3 royal face cards per suit (12 in total)
    for s in suits:
        for _ in full_range(1, 3):
            card = create_royal_card(s)
            deck.add_card(card)

    # final add 4 aces to deck (4 in total)
    for s in suits:
        card = create_ace_card(s)
        deck.add_card(card)

    return deck


class __Deck:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def is_populated(self):
        return len(self.cards) > 0

    def remove_random_card(self):
        if self.is_populated():
            card = random.choice(self.cards)
            self.cards.remove(card)
            return card

    def get_card_count(self):
        return len(self.cards)


class GameDeck:
    def __init__(self):
        self.decks = []

    def add_deck(self, card):
        self.decks.append(card)

    def is_populated(self):
        return len(self.decks) > 0

    def remove_random_card(self):
        if self.is_populated():
            # choose random deck
            i = random.randrange(len(self.decks))
            deck = self.decks[i]
            # choose random card
            card = deck.remove_random_card()
            self.decks[i] = deck
            return card

    def get_deck_count(self):
        return len(self.decks)

    def get_total_card_count(self):
        total = 0
        for d in self.decks:
            total += d.get_card_count()
        return total

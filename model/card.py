import enum


class CardType(enum.Enum):
    Number = 1
    Ace = 2
    Royal = 3


class Suit(enum.Enum):
    Spade = 1
    Clubs = 2
    Hearts = 3
    Diamonds = 4


def create_number_card(number, suit):
    return Card(number, number, suit, CardType.Number)


def create_ace_card(suit):
    return Card(11, 1, suit, CardType.Ace)


def create_royal_card(suit):
    return Card(10, 10, suit, CardType.Royal)


class Card:
    def __init__(self, value1, value2, suit, card_type):
        self.value1 = value1
        self.value2 = value2
        self.suit = suit
        self.card_type = card_type

    def to_string(self):
        return "value = " + str(self.value1) + " suit = " + str(self.suit) + " type = " + str(self.card_type)

from model.card import CardType


class Hand:
    def __init__(self):
        self.__cards = []
        self.__hidden = []
        self.__is_ace_in_hand = False
        self.__action = None

    def add_card(self, card):
        self.__cards.append(card)
        self.__is_ace_in_hand = True if card.card_type == CardType.Ace else self.__is_ace_in_hand

    def get_hand_total1(self):
        total = 0
        for card in self.__cards:
            total += card.value1
        return total

    def get_hand_total2(self):
        total = 0
        for card in self.__cards:
            total += card.value2
        return total

    def is_pair(self):
        if len(self.__cards) == 2:
            if self.__cards[0].value1 == self.__cards[1].value1:
                return True
        return False

    def is_hard(self):
        if self.__is_ace_in_hand:
            return False
        else:
            return True

    def add_face_down(self, card):
        self.__hidden.append(card)

    def is_cards_hidden(self):
        return len(self.__hidden) > 0

    def get_face_down(self):
        return self.__hidden.pop(0)

    def is_soft(self):
        return self.__is_ace_in_hand

    def get_max_total(self):
        return max(self.get_hand_total1(), self.get_hand_total2())

    def is_blackjack(self):
        return self.get_hand_total1() == 21 or self.get_hand_total2() == 21

    def is_busted(self):
        return (self.get_hand_total1() > 21 and self.get_hand_total1() == self.get_hand_total2()) \
               or self.get_hand_total2() > 21

    def cards_count(self):
        return len(self.__cards)

    def split_hand(self):
        # splits a single hand into two separate hands
        # only split hand if two cards in existing hand
        if len(self.__cards) == 2:
            half = len(self.__cards) // 2
            hand1 = Hand()
            hand2 = Hand()
            for card in self.__cards[:half]:
                hand1.add_card(card)
            for card in self.__cards[half:]:
                hand2.add_card(card)
            return hand1, hand2
        else:
            return None, None

    def set_action(self, action_type):
        self.__action = action_type

    def get_action(self):
        return self.__action

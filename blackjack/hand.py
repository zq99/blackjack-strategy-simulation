from model.card import CardType


class Hand:
    def __init__(self):
        self.cards = []
        self.hidden = []
        self.is_ace_in_hand = False

    def add_card(self, card):
        self.cards.append(card)
        self.is_ace_in_hand = True if card.card_type == CardType.Ace else self.is_ace_in_hand

    def get_hand_total1(self):
        total = 0
        for card in self.cards:
            total += card.value1
        return total

    def get_hand_total2(self):
        total = 0
        for card in self.cards:
            total += card.value2
        return total

    def is_pair(self):
        if len(self.cards) == 2:
            if self.cards[0].value1 == self.cards[1].value1:
                return True
        return False

    def is_hard(self):
        if self.is_ace_in_hand:
            return False
        else:
            return True

    def add_face_down(self,card):
        self.hidden.append(card)

    def is_cards_hidden(self):
        return len(self.hidden) > 0

    def get_face_down(self):
        return self.hidden.pop(0)

    def is_soft(self):
        return self.is_ace_in_hand

    def get_max_total(self):
        return max(self.get_hand_total1(), self.get_hand_total2())

    def is_blackjack(self):
        return self.get_hand_total1() == 21 or self.get_hand_total2() == 21

    def is_busted(self):
        return (self.get_hand_total1() > 21 and self.get_hand_total1() == self.get_hand_total2()) or self.get_hand_total2() > 21

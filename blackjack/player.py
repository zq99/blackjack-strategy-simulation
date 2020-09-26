from blackjack.score import Score


class Player:
    def __init__(self, strategy_type):
        self.strategy_type = strategy_type
        self.__hands = []
        self.__score = Score()

    def get_hands(self):
        return self.__hands

    def add_hand(self, hand):
        self.__hands.append(hand)

    def get_hand_count(self):
        return len(self.__hands)

    def add_card_hand(self, card, index):
        if index < self.get_hand_count():
            self.__hands[index].append(card)

    def add_card_to_first_hand(self, card):
        if self.get_hand_count() > 0:
            self.__hands[0].add_card(card)

    def get_score(self):
        return self.__score

    def discard_hands(self):
        self.__hands = []

    def get_strategy_name(self):
        return self.strategy_type.name

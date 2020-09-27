import enum

from blackjack.common import ActionType
import random as rand


class StrategyType(enum.Enum):
    BasicStrategy = 1
    Random = 2

    def __str__(self):
        return str(self.value)


class Strategy:

    def __init__(self, strategy_type=StrategyType.Random):
        self.type = strategy_type

    def evaluate(self, player_hand, dealer_hand):
        if self.type == StrategyType.BasicStrategy:
            return self.__basic_strategy(player_hand, dealer_hand)
        else:
            return self.__random_choice(player_hand)

    @staticmethod
    def __random_choice(player_hand):
        choices = [ActionType.Hit, ActionType.Double, ActionType.Surrender, ActionType.Stand]
        if player_hand.is_pair():
            choices.append(ActionType.Split)
        return rand.choice(choices)

    # noinspection PyUnusedLocal
    @staticmethod
    def __basic_strategy(player_hand, dealer_hand):

        # THIS NEEDS TO BE COMPLETED

        if player_hand.is_hard():
            if player_hand.get_max_total() >= 17:
                return ActionType.Stand
            else:
                return rand.choice(list(ActionType))
        elif player_hand.is_soft():
            return Strategy.__random_choice(player_hand)
        elif player_hand.is_pairs():
            return Strategy.__random_choice(player_hand)
        else:
            return Strategy.__random_choice(player_hand)

    def get_strategy(self):
        return str(self.type)

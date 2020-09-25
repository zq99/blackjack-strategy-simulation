import enum

from blackjack.common import ActionType
import random as rand


class StrategyType(enum.Enum):
    BasicStrategy = 1
    Random = 2


class Strategy:

    def __init__(self, strategy_type=StrategyType.Random):
        self.type = strategy_type

    def evaluate(self, player, dealer):
        if self.type == StrategyType.BasicStrategy:
            return self.__basic_strategy(player, dealer)
        else:
            return self.__random_choice()

    @staticmethod
    def __random_choice():
        return rand.choice(list(ActionType))

    @staticmethod
    def __basic_strategy(player, dealer):
        if player.is_hard():
            if player.get_max_total() >= 17:
                return ActionType.Stand
            else:
                return rand.choice(list(ActionType))
        elif player.is_soft():
            return rand.choice(list(ActionType))
        elif player.is_pairs():
            return rand.choice(list(ActionType))
        else:
            return rand.choice(list(ActionType))

    def get_strategy(self):
        return str(self.type)

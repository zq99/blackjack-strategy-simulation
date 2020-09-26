from blackjack.blackjack import Blackjack
from blackjack.player import Player
from blackjack.strategy import StrategyType
from blackjack.rules import Rules

# noinspection PyListCreation
def simulation():

    rules = Rules()
    blackjack = Blackjack(1000, 1,rules)

    players = []

    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.BasicStrategy))
    players.append(Player(StrategyType.BasicStrategy))

    players = blackjack.play(players)
    for player in players:
        print(player.get_score().to_string(), " ", player.get_strategy_name())


def main():
    simulation()


if __name__ == '__main__':
    main()

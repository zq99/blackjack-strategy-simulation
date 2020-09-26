from blackjack.blackjack import Blackjack
from blackjack.player import Player
from blackjack.strategy import StrategyType


# noinspection PyListCreation
def simulation():
    blackjack = Blackjack(1000, 1)

    players = []

    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.BasicStrategy))

    players = blackjack.play(players)
    for player in players:
        print(player.get_score().to_string(), " ", player.get_strategy_name())


def main():
    simulation()


if __name__ == '__main__':
    main()

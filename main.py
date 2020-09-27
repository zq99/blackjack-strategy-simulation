from blackjack.blackjack import Blackjack
from blackjack.player import Player
from blackjack.rules import Rules
from blackjack.strategy import StrategyType


# noinspection PyListCreation
def simulation():
    # creates a simulation of a game 1000 times featuring 4 players
    # playing different strategies, then prints their results out

    rules = Rules()
    blackjack = Blackjack(1000, 1, rules)

    players = []
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))

    players = blackjack.play(players)

    for player in players:
        print(player.get_score().to_string(), " ", player.get_strategy_name())


def main():
    simulation()


if __name__ == '__main__':
    main()

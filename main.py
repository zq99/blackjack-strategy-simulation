from simulation.blackjack import Blackjack
from simulation.player import Player
from simulation.rules import Rules
from simulation.strategy import StrategyType


# noinspection PyListCreation
def simulation():
    # creates a simulation of a game 1000 times featuring 4 players
    # playing different strategies, then prints their results out

    rules = Rules()
    rules.add_used_cards_back_into_deck = False
    blackjack = Blackjack(1000, 1, rules)

    players = []
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))

    players = blackjack.play(players)

    for counter, player in enumerate(players):
        print("player_" + str(counter + 1), " ", player.get_score().to_string(), " ", player.get_strategy_name())


def main():
    simulation()


if __name__ == '__main__':
    main()

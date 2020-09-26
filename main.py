from blackjack.blackjack import Blackjack
from blackjack.strategy import StrategyType


def simulation():

    blackjack = Blackjack(1000, 1)

    score = blackjack.play(StrategyType.BasicStrategy)
    print(score.to_string())

    score = blackjack.play(StrategyType.Random)
    print(score.to_string())


def main():
    simulation()


if __name__ == '__main__':
    main()

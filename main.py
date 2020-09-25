from blackjack.blackjack import play
from blackjack.strategy import StrategyType


def simulation():
    score = play(1000, 1, StrategyType.BasicStrategy)
    print(score.to_string())
    score = play(1000, 1, StrategyType.Random)
    print(score.to_string())


def main():
    simulation()


if __name__ == '__main__':
    main()

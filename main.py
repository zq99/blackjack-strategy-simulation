
from blackjack.blackjack import play
from blackjack.strategy import StrategyType


def main():
    score = play(1000, 1, StrategyType.BasicStrategy)
    print(score.to_string())
    score = play(1000, 1, StrategyType.Random)
    print(score.to_string())


if __name__ == '__main__':
    main()

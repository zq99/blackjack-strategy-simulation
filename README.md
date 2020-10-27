# Blackjack Game Strategy Simulator

This is an ongoing project to create a basic console based multi-player simulator to verify the results of playing different strategies when playing Blackjack.


## Background

The idea was to compare random play with basic strategy and card counting played both perfectly and imperfectly.


## Implementation

This is an example of a simulation featuring: 2 players playing randomly, with 1 deck, that is run 1000 times:

    blackjack = Blackjack(1000, 1, Rules())

    players = []
    players.append(Player(StrategyType.Random))
    players.append(Player(StrategyType.Random))

    players = blackjack.play(players)

    for counter, player in enumerate(players):
        print("player_" + str(counter + 1), " ", player.get_score().to_string(), " ", player.get_strategy_name())


## Things to complete

- Implement full Basic Strategy 
- Complete unit tests
- Allow game rules to be configured via the Rules object
- Export each round in simulation to csv

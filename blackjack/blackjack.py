from blackjack.common import ActionType
from blackjack.hand import Hand
from blackjack.score import Score
from blackjack.strategy import Strategy
from common.util import full_range
from model.deck import create_game_deck


def get_dealer_result(dealer, player, deck):
    while not dealer.is_busted():
        card = deck.remove_random_card()
        dealer.add_card(card)
        if dealer.is_blackjack() or dealer.get_max_total() > player.get_max_total():
            return True
    return False


def play(total_rounds, deck_count, strategy_type):
    score = Score()
    strategy = Strategy(strategy_type)

    counter = 0
    while counter < total_rounds:
        counter += 1
        deck = create_game_deck(deck_count)
        dealer = Hand()
        player = Hand()

        for _ in full_range(1, 2):
            player.add_card(deck.remove_random_card())
        dealer.add_card(deck.remove_random_card())

        if player.is_blackjack():
            score.add_to_player()
        else:
            while not player.is_busted():
                action = strategy.evaluate(player, dealer)
                if action == ActionType.Stand:
                    break
                elif action == ActionType.Hit or ActionType.Double:
                    card = deck.remove_random_card()
                    player.add_card(card)
                    if player.is_blackjack():
                        break

            if player.is_busted():
                score.add_to_dealer()
            elif not player.is_blackjack():
                dealer_result = get_dealer_result(dealer, player, deck)
                if dealer_result:
                    score.add_to_dealer()
                else:
                    score.add_to_player()
            else:
                score.add_to_player()
    return score

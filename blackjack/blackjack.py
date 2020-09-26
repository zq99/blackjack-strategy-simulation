from blackjack.common import ActionType
from blackjack.hand import Hand
from blackjack.score import Score
from blackjack.strategy import Strategy
from common.util import full_range
from model.deck import create_game_deck


class Blackjack:
    def __init__(self, total, decks):
        self.total_rounds = total
        self.deck_count = decks

    @staticmethod
    def __get_dealer_result(dealer, player, deck):
        # dealer issues cards to him/herself until
        # busted or player wins or dealer gets blackjack
        while not dealer.is_busted():
            card = dealer.get_face_down() if dealer.is_cards_hidden() else deck.remove_random_card()
            dealer.add_card(card)
            if dealer.is_blackjack() or dealer.get_max_total() > player.get_max_total():
                return True
        return False

    @staticmethod
    def __deal_to_player(player, dealer, deck, strategy):
        while not player.is_busted():
            action = strategy.evaluate(player, dealer)
            if action == ActionType.Stand:
                break
            elif action == ActionType.Hit or ActionType.Double:
                card = deck.remove_random_card()
                player.add_card(card)
                if player.is_blackjack():
                    break
        return player

    def play(self, strategy_type):
        # this method simulates each game of blackjack for however many times specified by 'total_rounds'
        score = Score()
        strategy = Strategy(strategy_type)

        counter = 0
        while counter < self.total_rounds:
            counter += 1
            deck = create_game_deck(self.deck_count)
            dealer = Hand()
            player = Hand()

            # deal cards to player
            for _ in full_range(1, 2):
                player.add_card(deck.remove_random_card())

            # deal cards to dealer
            dealer.add_card(deck.remove_random_card())
            dealer.add_face_down(deck.remove_random_card())

            if player.is_blackjack():
                score.add_to_player()
            else:

                player = self.__deal_to_player(player, dealer, deck, strategy)

                if player.is_busted():
                    score.add_to_dealer()
                elif not player.is_blackjack():
                    dealer_result = self.__get_dealer_result(dealer, player, deck)
                    if dealer_result:
                        score.add_to_dealer()
                    else:
                        score.add_to_player()
                else:
                    score.add_to_player()
        return score

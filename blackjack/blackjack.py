import enum

from blackjack.common import ActionType
from blackjack.hand import Hand
from blackjack.score import Score
from blackjack.strategy import Strategy
from common.util import full_range
from model.deck import create_game_deck


class ResultType(enum.Enum):
    PlayerWin = 1
    DealerWin = 2
    Push = 3


class Blackjack:
    def __init__(self, total, decks):
        self.total_rounds = total
        self.deck_count = decks

    @staticmethod
    def __get_result_against_dealer(dealer, player, deck):
        # dealer issues cards to him/herself until
        # busted or player wins or dealer gets blackjack
        while not dealer.is_busted():
            card = dealer.get_face_down() if dealer.is_cards_hidden() else deck.remove_random_card()
            dealer.add_card(card)
            if dealer.is_blackjack():
                if player.is_blackjack():
                    return ResultType.Push
                else:
                    return ResultType.DealerWin
            elif dealer.get_max_total() > player.get_max_total():
                return ResultType.DealerWin
        return ResultType.PlayerWin

    @staticmethod
    def __deal_more_cards_to_player(player, dealer, deck, strategy):
        while not player.is_busted():
            action = strategy.evaluate(player, dealer)
            if action == ActionType.Stand:
                break
            elif action == ActionType.Hit or ActionType.Double:
                card = deck.remove_random_card()
                player.add_card(card)
                if player.is_blackjack():
                    break
        return player, deck

    @staticmethod
    def __deal_initial_cards(player, dealer, deck):
        # deal cards to player
        for n in full_range(1, 2):
            player.add_card(deck.remove_random_card())

        # deal cards to dealer
        dealer.add_card(deck.remove_random_card())
        dealer.add_face_down(deck.remove_random_card())
        return player, dealer, deck

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

            player, dealer, deck = self.__deal_initial_cards(player, dealer, deck)

            player, deck = self.__deal_more_cards_to_player(player, dealer, deck, strategy)

            if player.is_busted():
                score.add_to_dealer()
            else:
                result = self.__get_result_against_dealer(dealer, player, deck)
                if result == ResultType.DealerWin:
                    score.add_to_dealer()
                elif result == ResultType.PlayerWin:
                    score.add_to_player()
                else:
                    score.add_to_push()
        return score

import enum

from blackjack.common import ActionType
from blackjack.dealer import Dealer
from blackjack.hand import Hand
from blackjack.strategy import Strategy
from model.deck import create_deck


class ResultType(enum.Enum):
    PlayerWin = 1
    DealerWin = 2
    Push = 3


class Blackjack:
    def __init__(self, total, decks):
        self.total_rounds = total
        self.deck_count = decks

    @staticmethod
    def __get_result_against_dealer(dealer_hand, player_hand):
        if dealer_hand.is_blackjack():
            if player_hand.is_blackjack():
                return ResultType.Push
            else:
                return ResultType.DealerWin
        elif dealer_hand.get_max_total() > player_hand.get_max_total():
            return ResultType.DealerWin
        return ResultType.PlayerWin

    @staticmethod
    def __deal_more_cards_to_dealer(dealer, deck, highest_player_total):
        while not dealer.get_hand().is_busted():
            dealer_hand = dealer.get_hand()
            card = dealer_hand.get_face_down() if dealer_hand.is_cards_hidden() else deck.remove_random_card()
            dealer_hand.add_card(card)
            if dealer_hand.is_blackjack():
                break
            elif dealer_hand.get_max_total() > highest_player_total:
                break
        return dealer

    @staticmethod
    def __deal_more_cards_to_players(players, dealer, deck):
        max_total = 0
        for player in players:
            strategy = Strategy(player.strategy_type)
            for player_hand in player.get_hands():
                while not player_hand.is_busted():
                    action = strategy.evaluate(player_hand, dealer.get_hand())
                    if action == ActionType.Stand:
                        break
                    elif action == ActionType.Hit or ActionType.Double:
                        card = deck.remove_random_card()
                        player_hand.add_card(card)
                        if player_hand.is_blackjack():
                            break
                max_total = max(max_total, player_hand.get_max_total())
        return players, deck, max_total

    @staticmethod
    def __deal_initial_cards(players, dealer, deck):
        # dealing card order methodology:
        # https://healy.econ.ohio-state.edu/blackjack/table/dealing.html

        # deal 1st card to players
        for player in players:
            player.add_card_to_first_hand(deck.remove_random_card())

        # deal 1st down card to dealer
        dealer.get_hand().add_face_down(deck.remove_random_card())

        # deal 2nd card to players
        for player in players:
            player.add_card_to_first_hand(deck.remove_random_card())

        # deal 2nd card to dealer
        dealer.get_hand().add_card(deck.remove_random_card())
        return players, dealer, deck

    @staticmethod
    def __initialize_players(players):
        for player in players:
            player.add_hand(Hand())
        return players

    def play(self, players):

        # this method simulates each game of blackjack

        counter = 0
        while counter < self.total_rounds:
            counter += 1
            deck = create_deck(self.deck_count)

            dealer = Dealer()
            players = self.__initialize_players(players)

            players, dealer, deck = self.__deal_initial_cards(players, dealer, deck)

            players, deck, highest_total = self.__deal_more_cards_to_players(players, dealer, deck)

            dealer = self.__deal_more_cards_to_dealer(dealer, deck, highest_total)

            for player in players:
                for player_hand in player.get_hands():
                    if player_hand.is_busted():
                        player.get_score().add_to_losses()
                    else:
                        result = self.__get_result_against_dealer(dealer.get_hand(), player_hand)
                        if result == ResultType.DealerWin:
                            player.get_score().add_to_losses()
                        elif result == ResultType.PlayerWin:
                            player.get_score().add_to_wins()
                        else:
                            player.get_score().add_to_push()
                player.discard_hands()
        return players

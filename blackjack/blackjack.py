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
    def __init__(self, total, pack_count, rules):
        self.total_rounds = total
        self.deck_count = pack_count
        self.rules = rules

    @staticmethod
    def __compare_dealer_and_player_hands(dealer_hand, player_hand):
        # evaluation function to determine winners and losers in the game
        if dealer_hand.is_blackjack():
            return ResultType.Push if player_hand.is_blackjack() else ResultType.DealerWin
        elif dealer_hand.get_max_total() > player_hand.get_max_total():
            return ResultType.DealerWin
        return ResultType.PlayerWin

    @staticmethod
    def __deal_more_cards_to_dealer(dealer, deck, highest_player_total):
        # dealer_hand deals to him/herself until busted or until each player_hand is beaten
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
        # each player_hand gets more cards from the dealer
        # depending on what strategy they are implementing
        highest_total = 0
        for player in players:
            strategy = Strategy(player.strategy_type)
            for player_hand in player.get_hands():
                while not player_hand.is_busted() and player_hand.get_action() != ActionType.Surrender:
                    action = strategy.evaluate(player_hand, dealer.get_hand())
                    player_hand.set_action(action)
                    if action == ActionType.Stand:
                        break
                    elif action == ActionType.Hit or ActionType.Double:
                        card = deck.remove_random_card()
                        player_hand.add_card(card)
                        if player_hand.is_blackjack():
                            break
                    elif action == ActionType.Split:
                        hand1, hand2 = player_hand.split_hand()
                        player.add_hand(hand1)
                        player.add_hand(hand2)
                        player.remove_hand(player_hand)
                highest_total = max(highest_total, player_hand.get_max_total())
        return players, deck, highest_total

    @staticmethod
    def __deal_initial_cards(players, dealer, deck):
        # dealing card order methodology:
        # https://healy.econ.ohio-state.edu/blackjack/table/dealing.html

        # deal 1st card to players
        for player in players:
            player.add_card_to_first_hand(deck.remove_random_card())

        # deal 1st down card to dealer_hand
        dealer.get_hand().add_face_down(deck.remove_random_card())

        # deal 2nd card to players
        for player in players:
            player.add_card_to_first_hand(deck.remove_random_card())

        # deal 2nd card to dealer_hand
        dealer.get_hand().add_card(deck.remove_random_card())
        return players, dealer, deck

    @staticmethod
    def __initialize_players(players):
        for player in players:
            player.add_hand(Hand())
        return players

    def play(self, players):
        # this method simulates each game of blackjack
        # input: list of players
        # output: list of players with their results

        for n in range(0, self.total_rounds):

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
                    elif player_hand.get_action == ActionType.Surrender:
                        player.get_score().add_to_losses()
                    else:
                        comparison = self.__compare_dealer_and_player_hands(dealer.get_hand(), player_hand)
                        if comparison == ResultType.DealerWin:
                            player.get_score().add_to_losses()
                        elif comparison == ResultType.PlayerWin:
                            player.get_score().add_to_wins()
                        else:
                            player.get_score().add_to_push()
                player.discard_hands()
        return players

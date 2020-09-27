import unittest
from model.deck import *


class DeckTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

        deck = create_deck(1)
        self.assertEqual(52, deck.get_total_card_count())
        self.assertEqual(51, deck.get_total_card_count())
        self.assertEqual(1, deck.get_deck_count())

    def split_test(self):
        from simulation.hand import Hand
        from model.card import create_ace_card, Suit
        hand = Hand()
        card1 = create_ace_card(Suit.Spade)
        card2 = create_ace_card(Suit.Hearts)
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(2, hand.cards_count())
        self.assertTrue(hand.is_pair())
        hand1, hand2 = hand.split_hand()
        self.assertEqual(hand1.cards_count(), 1)
        self.assertEqual(hand2.cards_count(), 1)

        for card in hand1.cards:
            self.assertEqual("value = 11 suit = Suit.Spade type = CardType.Ace", card.to_string())

        for card in hand2.cards:
            self.assertEqual("value = 11 suit = Suit.Hearts type = CardType.Ace", card.to_string())


if __name__ == '__main__':
    unittest.main()

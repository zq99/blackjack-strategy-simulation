import unittest
from model.deck import *


class DeckTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

        deck = create_game_deck(1)
        self.assertEqual(52, deck.get_total_card_count())
        self.assertEqual(51, deck.get_total_card_count())
        self.assertEqual(1, deck.get_deck_count())


if __name__ == '__main__':
    unittest.main()

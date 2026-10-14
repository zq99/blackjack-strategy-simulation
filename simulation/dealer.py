from simulation.hand import Hand


class Dealer:
    def __init__(self):
        self.__hand = Hand()

    def get_hand(self) -> Hand:
        return self.__hand


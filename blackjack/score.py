from common.util import get_percentage


class Score:
    def __init__(self):
        self.player = 0
        self.dealer = 0

    def add_to_player(self):
        self.player += 1

    def add_to_dealer(self):
        self.dealer += 1

    def get_total(self):
        return self.dealer + self.player

    def get_win_percent(self):
        return get_percentage(self.player, self.get_total())

    def to_string(self):
        return "player = " + str(self.player) + " dealer = " + str(self.dealer) + " total = " + str(self.get_total()) + " win% = " + str(self.get_win_percent())

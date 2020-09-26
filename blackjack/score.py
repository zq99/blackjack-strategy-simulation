from common.util import get_percentage


class Score:
    def __init__(self):
        self.player = 0
        self.dealer = 0
        self.push = 0

    def add_to_player(self):
        self.player += 1

    def add_to_dealer(self):
        self.dealer += 1

    def add_to_push(self):
        self.push += 1

    def get_total(self):
        return self.dealer + self.player + self.push

    def get_win_percent(self):
        return get_percentage(self.player, self.get_total())

    def to_string(self):
        return "player = " + str(self.player) + " dealer = " + str(self.dealer) + " push = " + str(self.push) + " total = " + str(self.get_total()) + " win% = " + str(self.get_win_percent())

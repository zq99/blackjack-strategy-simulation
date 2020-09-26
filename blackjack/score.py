from common.util import get_percentage


class Score:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.push = 0

    def add_to_wins(self):
        self.wins += 1

    def add_to_losses(self):
        self.losses += 1

    def add_to_push(self):
        self.push += 1

    def get_total(self):
        return self.losses + self.wins + self.push

    def get_win_percent(self):
        return get_percentage(self.wins, self.get_total())

    def to_string(self):
        return "wins = " + str(self.wins) + " losses = " + str(self.losses) + " push = " + str(self.push) + " total = " + str(self.get_total()) + " wins% = " + str(self.get_win_percent())

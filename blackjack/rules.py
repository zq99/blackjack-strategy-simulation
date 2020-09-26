class Rules:
    def __init__(self):
        self.__replace_cards = False

    def get_replace_cards(self):
        return self.__replace_cards

    def set_replace_cards(self,value):
        self.__replace_cards = value

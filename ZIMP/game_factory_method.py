from start import Start
from load_tiles import LoadTiles
from load_cards import LoadCards
from get_game import GetGame


# Factory Method
class CommandFactory:
    def start(self):
        return Start()

    def tiles(self):
        return LoadTiles()

    def cards(self):
        return LoadCards()

    def get_game(self):
        return GetGame()


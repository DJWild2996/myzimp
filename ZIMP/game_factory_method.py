from start import Start
from load_tiles import LoadTiles
from load_cards import LoadCards
from get_game import GetGame
from player_info import PlayerInfo


# Factory Method
class CommandFactory:
    def start_game(self):
        return Start()

    def load_tiles(self):
        return LoadTiles()

    def Load_cards(self):
        return LoadCards()

    def get_game(self):
        return GetGame()

    def get_player_status(self):
        return PlayerInfo()



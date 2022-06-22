from start import Start
from load_tiles import LoadTiles
from load_cards import LoadCards
from get_game import GetGame
from player_info import PlayerInfo
from draw_tile import DrawTiles
from trigger_dev_card import TriggerDevCard
from trigger_attack import TriggerAttack


# Factory Method / Concrete Creator
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

    def draw_tile(self):
        return DrawTiles()

    def trigger_dev_card(self):
        return TriggerDevCard()

    def trigger_attack(self):
        return TriggerAttack()



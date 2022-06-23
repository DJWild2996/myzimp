from abstract_creator import Creator
from start import Start
from load_tiles import LoadTiles
from load_cards import LoadCards
from get_game import GetGame
from player_info import PlayerInfo
from draw_tile import DrawTiles
from trigger_dev_card import TriggerDevCard
from trigger_attack import TriggerAttack


# Factory Method / Concrete Creator
class ConcreteCreator1(Creator):
    def factory_method(self):
        return Start()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return LoadTiles()


class ConcreteCreator3(Creator):
    def factory_method(self):
        return LoadCards()


class ConcreteCreator4(Creator):
    def factory_method(self):
        return GetGame()


class ConcreteCreator5(Creator):
    def factory_method(self):
        return PlayerInfo()


class ConcreteCreator6(Creator):
    def factory_method(self):
        return DrawTiles()


class ConcreteCreator7(Creator):
    def factory_method(self):
        return TriggerDevCard()


class ConcreteCreator8(Creator):
    def factory_method(self):
        return TriggerAttack()

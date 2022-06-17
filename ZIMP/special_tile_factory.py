from abstract_factory import BaseAbstractFactory
from special_indoor_tile import SpecialIndoorTile
from special_outdoor_tile import SpecialOutdoorTile


# ConcreteClass
class SpecialTileFactory(BaseAbstractFactory):
    def __init__(self):
        return SpecialIndoorTile()

    def set_x(self):
        return SpecialIndoorTile()

    def set_y(self):
        return SpecialIndoorTile()

    def change_door_position(self):
        return SpecialIndoorTile()

    def set_entrance(self):
        return SpecialIndoorTile()

    def rotate_entrance(self):
        return SpecialIndoorTile()

    def rotate_tile(self):
        return SpecialIndoorTile()

    def __init__(self):
        return SpecialOutdoorTile()

    def set_x(self):
        return SpecialOutdoorTile()

    def set_y(self):
        return SpecialOutdoorTile()

    def change_door_position(self):
        return SpecialOutdoorTile()

    def set_entrance(self):
        return SpecialOutdoorTile()

    def rotate_entrance(self):
        return SpecialOutdoorTile()

    def rotate_tile(self):
        return SpecialOutdoorTile()

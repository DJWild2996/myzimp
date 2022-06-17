from abstract_factory import BaseAbstractFactory
from normal_indoor_tile import NormalIndoorTile
from normal_outdoor_tile import NormalOutdoorTile


# ConcreteClass
class NormalTileFactory(BaseAbstractFactory):
    def __init__(self):
        return NormalIndoorTile()

    def set_x(self):
        return NormalIndoorTile()

    def set_y(self):
        return NormalIndoorTile()

    def change_door_position(self):
        return NormalIndoorTile()

    def set_entrance(self):
        return NormalIndoorTile()

    def rotate_entrance(self):
        return NormalIndoorTile()

    def rotate_tile(self):
        return NormalIndoorTile()

    def __init__(self):
        return NormalOutdoorTile()

    def set_x(self):
        return NormalOutdoorTile()

    def set_y(self):
        return NormalOutdoorTile()

    def change_door_position(self):
        return NormalOutdoorTile()

    def set_entrance(self):
        return NormalOutdoorTile()

    def rotate_entrance(self):
        return NormalOutdoorTile()

    def rotate_tile(self):
        return NormalOutdoorTile()

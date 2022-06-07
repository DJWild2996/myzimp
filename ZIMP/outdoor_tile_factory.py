from abstract_factory import BaseAbstractFactory
from outdoor_tile import OutdoorTile


# ConcreteClass
class OutdoorTileFactory(BaseAbstractFactory):
    def __init__(self):
        return OutdoorTile()

    def set_x(self):
        return OutdoorTile()

    def set_y(self):
        return OutdoorTile()

    def change_door_position(self):
        return OutdoorTile()

    def set_entrance(self):
        return OutdoorTile()

    def rotate_entrance(self):
        return OutdoorTile()

    def rotate_tile(self):
        return OutdoorTile()

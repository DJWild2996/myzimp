from abstract_factory import BaseAbstractFactory
from indoor_tile import IndoorTile


# ConcreteClass
class IndoorTileFactory(BaseAbstractFactory):
    def __init__(self, name, x=16, y=16, effect=None, doors=None, entrance=None):
        return IndoorTile()

    def set_x(self):
        return IndoorTile()

    def set_y(self):
        return IndoorTile()

    def change_door_position(self):
        return IndoorTile()

    def set_entrance(self):
        return IndoorTile()

    def rotate_entrance(self):
        return IndoorTile()

    def rotate_tile(self):
        return IndoorTile()

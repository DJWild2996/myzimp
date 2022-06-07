from indoor_tile import IndoorTile
from abstract_factory import BaseAbstractFactory


# ConcreteClass
class IndoorTileFactory(BaseAbstractFactory):
    def __init__(self, name, x=16, y=16, effect=None, doors=None, entrance=None):  # Added default arguments - Daniel
        if doors is None:
            doors = []
        self.name = name
        self.x = x
        self.y = y
        self.effect = effect
        self.doors = doors
        self.entrance = entrance

    def set_x(self):
        return IndoorTile.set_x()

    def set_y(self):
        return IndoorTile.set_y()

    def change_door_position(self):
        return IndoorTile.change_door_position()

    def set_entrance(self):
        return IndoorTile.set_entrance()

    def rotate_entrance(self):
        return IndoorTile.rotate_tile()

    def rotate_tile(self):
        return IndoorTile.rotate_tile()

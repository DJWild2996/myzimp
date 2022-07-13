from abc import ABCMeta, abstractmethod


# AbstractProductA
class TileType(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def set_x(self):
        pass

    @abstractmethod
    def set_y(self):
        pass

    @abstractmethod
    def change_door_position(self):
        pass

    @abstractmethod
    def set_entrance(self):
        pass

    @abstractmethod
    def rotate_entrance(self):
        pass

    @abstractmethod
    def rotate_tile(self):
        pass

from abc import ABCMeta, abstractmethod


# AbstractProductB
class TileAction(metaclass=ABCMeta):
    @abstractmethod
    def tile_action(self):
        pass

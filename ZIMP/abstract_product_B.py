from abc import ABCMeta, abstractmethod


# AbstractProductB
class TileProduct(metaclass=ABCMeta):
    @abstractmethod
    def tile_action(self):
        pass

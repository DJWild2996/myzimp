from abc import ABCMeta, abstractmethod


# AbstractProductA
class TileProduct(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass



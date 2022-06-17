from abc import ABCMeta, abstractmethod


# AbstractProductA
class SpecialTileProduct(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass



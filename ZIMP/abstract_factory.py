from abc import ABCMeta, abstractmethod


# AbstractFactory
class BaseAbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_tile_type(self):
        pass

    @abstractmethod
    def create_tile_action(self):
        pass

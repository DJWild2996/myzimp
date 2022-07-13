from abc import ABCMeta, abstractmethod


# AbstractFactory
class BaseAbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

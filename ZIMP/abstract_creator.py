from abc import ABC, abstractmethod


# Abstract Product
class Creator(ABC):
    @abstractmethod
    def create_product(self):
        pass

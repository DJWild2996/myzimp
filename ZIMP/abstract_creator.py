from abc import ABC, abstractmethod


# Abstract Product
class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

from abc import ABC, abstractmethod


# Abstract Product
class AbstractCommands(ABC):
    @abstractmethod
    def command(self):
        pass

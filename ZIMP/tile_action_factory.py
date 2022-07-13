from abstract_factory import BaseAbstractFactory
from search_for_totem import SearchForTotem
from bury_totem import BuryTotem


# ConcreteClass
class TileActionFactory(BaseAbstractFactory):

    def create_product_a(self):
        return SearchForTotem()

    def create_product_b(self):
        return BuryTotem()

from abstract_factory import BaseAbstractFactory
from indoor_tile import IndoorTile
from outdoor_tile import OutdoorTile


# ConcreteClass
class TileFactory(BaseAbstractFactory):

    def create_product_a(self):
        return IndoorTile()

    def create_product_b(self):
        return OutdoorTile()

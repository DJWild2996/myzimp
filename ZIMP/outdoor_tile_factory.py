from abstract_factory import BaseAbstractFactory
from outdoor_tile import OutdoorTile
from bury_totem import BuryTotem


# ConcreteClass
class OutdoorTileFactory(BaseAbstractFactory):

    def create_tile_type(self):
        return OutdoorTile()

    def create_tile_action(self):
        return BuryTotem()

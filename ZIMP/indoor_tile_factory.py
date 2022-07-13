from abstract_factory import BaseAbstractFactory
from indoor_tile import IndoorTile
from search_for_totem import SearchForTotem


# ConcreteClass
class IndoorTileFactory(BaseAbstractFactory):

    def create_tile_type(self):
        return IndoorTile()

    def create_tile_action(self):
        return SearchForTotem()

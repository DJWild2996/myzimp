from abstract_commands import AbstractCommands
from directions import Direction as myD
import pandas as pd
from tile_factory import IndoorTile
from tile_factory import OutdoorTile


# Product B
class LoadTiles(AbstractCommands):
    def command(self):
        try:
            excel_data = pd.read_excel('Tiles.xlsx')
            tiles = []
            for name in excel_data.iterrows():
                tiles.append(name[1].tolist())
            for tile in tiles:
                doors = self.resolve_doors(tile[3], tile[4], tile[5], tile[6])
                if tile[2] == "Outdoor":
                    new_tile = OutdoorTile(tile[0], tile[1], doors)
                    if tile[0] == "Patio":
                        new_tile.set_entrance(myD.NORTH)
                    self.outdoor_tiles.append(new_tile)
                if tile[2] == "Indoor":
                    new_tile = IndoorTile(tile[0], tile[1], doors)
                    if tile[0] == "Dining Room":
                        new_tile.set_entrance(myD.NORTH)
                    self.indoor_tiles.append(new_tile)

        except FileNotFoundError as e:
            print("ERROR: File not found please check Excel file name", e)
        except OSError as e:
            print("ERROR: Unable to access file please check file location", e)

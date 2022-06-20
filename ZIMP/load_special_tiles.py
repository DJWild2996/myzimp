from abstract_game import AbstractCommands
from directions import Direction as dir
import pandas as pd
from special_tile_factory import SpecialIndoorTile
from special_tile_factory import SpecialOutdoorTile


class LoadSpecialTiles(AbstractCommands):
    def command(self):
        try:
            excel_data = pd.read_excel('Tiles.xlsx')
            tiles = []
            for name in excel_data.iterrows():
                tiles.append(name[1].tolist())
            for tile in tiles:
                doors = self.resolve_doors(tile[3], tile[4], tile[5], tile[6])
                if tile[2] == "Outdoor":
                    new_tile = SpecialOutdoorTile(tile[0], tile[1], doors)
                    if tile[0] == "Patio":
                        new_tile.set_entrance(dir.NORTH)
                    self.outdoor_tiles.append(new_tile)
                if tile[2] == "Indoor":
                    new_tile = SpecialIndoorTile(tile[0], tile[1], doors)
                    if tile[0] == "Dining Room":
                        new_tile.set_entrance(dir.NORTH)
                    self.indoor_tiles.append(new_tile)

        except FileNotFoundError as e:
            print("ERROR: File not found please check Excel file name", e)
        except OSError as e:
            print("ERROR: Unable to access file please check file location", e)
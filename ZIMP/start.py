from abstract_commands import AbstractCommands


# Product A
class Start(AbstractCommands):
    def __init__(self, chosen_tile=None, state="Starting"):
        self.state = None
        self.chosen_tile = chosen_tile
        self.state = state

    def command(self):
        self.load_tiles()
        self.load_dev_cards()
        print('The dead walk the earth. You must search the house for the Evil Temple, and find the zombie totem. Then '
              'take the totem outside, and bury it in the Graveyard, all before the clock strikes midnight. ')
        for tile in self.indoor_tiles:
            if tile.name == 'Foyer':
                self.chosen_tile = tile
                self.state = "Rotating"
                break

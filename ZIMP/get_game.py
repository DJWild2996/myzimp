from abstract_commands import AbstractCommands


# Product D
class GetGame(AbstractCommands):
    def command(self):
        try:
            s = ''
            f = ''
            if self.state == "Moving":
                s = "In this state you can move by typing 'n, e, s, w' "
            if self.state == "Rotating":
                s = "Type 'rotate' until the door of the current tile are aligned with the new tile" \
                    " Once you are happy with the door position you can place the tile by typing 'place' "
            if self.state == "Choosing Door":
                s = "There are no doors you can go through in this room, you will have to make your-own" \
                    "Choose where to place a new door by typing 'choose' and a direction 'n, e, s, w' "
            if self.state == "Drawing Dev Card":
                s = "Type 'draw' to draw a random card this may lead to a zombie attack, and item or nothing depending on the time"
            for door in self.chosen_tile.doors:
                f += door.name + ', '
            return print(f' Your current tile is {self.chosen_tile.name}, the available doors in this room are {f}\n '
                         f'The state is {self.state}. {s} \n Special Entrances : {self.chosen_tile.entrance}')

        except AttributeError as e:
            print("ERROR: Unable to load game states, please try again", e)
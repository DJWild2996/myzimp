from abstract_commands import AbstractCommands


# Product A
class PlayerInfo(AbstractCommands):
    def __init__(self, player):
        self.state = None
        self.player = player

    def command(self):
        return print(f'It is {self.get_time()} pm \n'
                     f'The player currently has {self.player.get_health()} health \n'
                     f'The player currently has {self.player.get_attack()} attack \n'
                     f'The players items are {self.player.get_items()}\n'
                     f'The game state is {self.state}')

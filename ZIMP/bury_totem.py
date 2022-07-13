from abstract_product_B import TileProduct


# ConcreteProductB1
class BuryTotem(TileProduct):
    def __init__(self, game, player, time=9):

        self.game = game
        self.player = player
        self.time = time

    def tile_action(self):
        if self.game.get_current_tile().name == "Graveyard":
            if self.player.has_totem:
                self.game.trigger_dev_card(self.game.time)
                if self.player.health != 0:
                    print("You Won")
                    self.game.state = "Game Over"
        else:
            print("Cannot bury totem here")

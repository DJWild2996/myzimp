from abstract_product_B import TileProduct


# ConcreteProductB1
class SearchForTotem(TileProduct):
    def __init__(self, game, player, time=9):

        self.game = game
        self.player = player
        self.time = time

    def tile_action(self):
        if self.game.get_current_tile().name == "Evil Temple":
            if self.player.has_totem:
                print("player already has the totem")
                return
            else:
                self.game.trigger_dev_card(self.time)
                self.player.found_totem()
        else:
            print("You cannot search for a totem in this room")
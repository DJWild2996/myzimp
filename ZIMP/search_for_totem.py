from abstract_product_B import TileAction


# ConcreteProductB1
class SearchForTotem(TileAction):
    def __init__(self, game, player):

        self.game = game
        self.player = player
        self.type = "Indoor"

    def tile_action(self):
        if self.get_current_tile().type == "Indoor":
            if self.get_current_tile().name == "Evil Temple":
                if self.player.has_totem:
                    print("player already has the totem")
                    return
                else:
                    self.game.trigger_dev_card(self.game.time)
                    self.player.found_totem()
            else:
                print("You cannot search for a totem in this room")

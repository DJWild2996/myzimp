from directions import Direction as myD
from game_factory_method import Start
from game_factory_method import LoadTiles
from game_factory_method import LoadCards
from game_factory_method import GetGame
from game_factory_method import PlayerInfo
from game_factory_method import DrawTiles
from game_factory_method import TriggerDevCard
from game_factory_method import TriggerAttack
from indoor_tile_factory import SearchForTotem
from outdoor_tile_factory import BuryTotem


class Game:
    def __init__(self, player, time=9, game_map=None, indoor_tiles=None, outdoor_tiles=None, chosen_tile=None,
                 dev_cards=None, state="Starting", current_move_direction=None,
                 can_cower=True):
        if indoor_tiles is None:
            indoor_tiles = []
        if outdoor_tiles is None:
            outdoor_tiles = []
        if dev_cards is None:
            dev_cards = []
        if game_map is None:
            game_map = {}

        self.player = player
        self.time = time
        self.indoor_tiles = indoor_tiles
        self.outdoor_tiles = outdoor_tiles
        self.dev_cards = dev_cards
        self.tiles = game_map
        self.chosen_tile = chosen_tile
        self.state = state
        self.current_move_direction = current_move_direction
        self.current_zombies = 0
        self.can_cower = can_cower
        self.room_item = None

    #  Puts the game into starting state using users input of the start command
    def start_game(self):
        Start.command(self)

    #  Loads the games different states and assigns command line text to them
    def get_game(self):
        GetGame.command(self)

    #  Shows player there current stats
    def get_player_status(self):
        PlayerInfo.command(self)

    def get_time(self):
        return self.time

    # Load tiles from the Excel file, added error checking - Daniel
    def load_tiles(self):
        LoadTiles.command(self)

    # Lets player draw tiles as the move- Daniel
    def draw_tile(self, x, y):
        DrawTiles.command(self, x, y)

    # Load cards from Excel file, added error checking - Daniel
    def load_dev_cards(self):
        LoadCards.command(self)

    #  Moves the player to a new location when in the right state
    def move_player(self, x, y):
        self.player.set_y(y)
        self.player.set_x(x)
        if self.state == "Running":
            self.state = "Moving"
        else:
            self.state = "Drawing Dev Card"

    def get_tile_at(self, x, y):
        return self.tiles[(x, y)]

    #  Lets player select a direction to move using tile doors
    def select_move(self, direction):
        x, y = self.get_destination_coords(direction)
        if self.check_for_door(direction):
            self.current_move_direction = direction
            if self.check_for_room(x, y) is False:
                if self.state == "Running":
                    return print("Can only run into a discovered room")
                else:
                    self.draw_tile(x, y)
                    self.state = "Rotating"
            if self.check_for_room(x, y):
                if self.check_indoor_outdoor_move(self.get_current_tile().type, self.get_tile_at(x, y).type):
                    return print("Cannot Move this way")
                else:
                    self.move_player(x, y)

    def check_indoor_outdoor_move(self, current_type, move_type):
        if current_type != move_type and self.get_current_tile().name != "Patio" or "Dining Room":
            return False

    def get_destination_coords(self, direction):
        if direction == myD.NORTH:
            return self.player.get_x(), self.player.get_y() - 1
        if direction == myD.SOUTH:
            return self.player.get_x(), self.player.get_y() + 1
        if direction == myD.EAST:
            return self.player.get_x() + 1, self.player.get_y()
        if direction == myD.WEST:
            return self.player.get_x() - 1, self.player.get_y()

    def check_for_door(self, direction):
        if direction in self.get_current_tile().doors:
            return True
        else:
            return False

    def check_for_room(self, x, y):
        if (x, y) not in self.tiles:
            return False
        else:
            self.chosen_tile = self.tiles[(x, y)]
            return True

    def check_doors_align(self, direction):
        if self.chosen_tile.name == "Foyer":
            return True
        if direction == myD.NORTH:
            if myD.SOUTH not in self.chosen_tile.doors:
                return False
        if direction == myD.SOUTH:
            if myD.NORTH not in self.chosen_tile.doors:
                return False
        if direction == myD.WEST:
            if myD.EAST not in self.chosen_tile.doors:
                return False
        elif direction == myD.EAST:
            if myD.WEST not in self.chosen_tile.doors:
                return False
        return True

    def check_entrances_align(self):
        if self.get_current_tile().entrance == myD.NORTH:
            if self.chosen_tile.entrance == myD.SOUTH:
                return True
        if self.get_current_tile().entrance == myD.SOUTH:
            if self.chosen_tile.entrance == myD.NORTH:
                return True
        if self.get_current_tile().entrance == myD.WEST:
            if self.chosen_tile.entrance == myD.EAST:
                return True
        if self.get_current_tile().entrance == myD.EAST:
            if self.chosen_tile.entrance == myD.WEST:
                return True
        return print(" Dining room and Patio entrances dont align")

    def check_dining_room_has_exit(self):
        tile = self.chosen_tile
        if tile.name == "Dining Room":
            if self.current_move_direction == myD.NORTH and tile.entrance == myD.SOUTH:
                return False
            if self.current_move_direction == myD.SOUTH and tile.entrance == myD.NORTH:
                return False
            if self.current_move_direction == myD.EAST and tile.entrance == myD.WEST:
                return False
            if self.current_move_direction == myD.WEST and tile.entrance == myD.EAST:
                return False
        else:
            return True

    def place_tile(self, x, y):
        tile = self.chosen_tile
        self.tiles[(x, y)] = tile
        self.state = "Moving"
        if tile.type == "Outdoor":
            self.outdoor_tiles.pop(self.outdoor_tiles.index(tile))
        elif tile.type == "Indoor":
            self.indoor_tiles.pop(self.indoor_tiles.index(tile))

    def get_current_tile(self):
        return self.tiles[self.player.get_x(), self.player.get_y()]

    def rotate(self):
        tile = self.chosen_tile
        tile.rotate_tile()
        if tile.name == "Foyer":
            return
        if self.get_current_tile().name == "Dining Room" or "Patio":
            tile.rotate_entrance()

    def trigger_dev_card(self, time):
        TriggerDevCard.command(self, time)

    def trigger_attack(self, *item):
        TriggerAttack.command(self, *item)

    def trigger_run(self, direction, health_lost=-1):
        self.state = "Running"
        self.select_move(direction)
        if self.state == "Moving":
            self.player.add_health(health_lost)
            print(f"You run away from the zombies, and lose {health_lost} health")
            self.can_cower = True
            if self.get_current_tile().name == "Garden" or "Kitchen":
                self.trigger_room_effect(self.get_current_tile().name)
        else:
            self.state = "Attacking"

    def trigger_room_effect(self, room_name):
        if room_name == "Garden":
            self.player.add_health(1)
            print(f"After ending your turn in the {room_name} you have gained one health")
            self.state = "Moving"
        if room_name == "Kitchen":
            self.player.add_health(1)
            print(f"After ending your turn in the {room_name} you have gained one health")
            self.state = "Moving"

    def trigger_cower(self):
        if self.can_cower:
            self.player.add_health(3)
            self.dev_cards.pop(0)
            self.state = "Moving"
            print("You cower in fear, gaining 3 health, but lose time with the dev card")
        else:
            return print("Cannot cower during a zombie door attack")

    def drop_item(self, old_item):
        for item in self.player.get_items():
            if item[0] == old_item:
                self.player.remove_item(item)
                print(f"You dropped the {old_item}")
                self.state = "Moving"
                return
        print("That item is not in your inventory")

    def use_item(self, *item):
        if "Can of Soda" in item:
            self.player.add_health(2)
            self.drop_item("Can of Soda")
            print("Used Can of Soda, gained 2 health")
        elif "Gasoline" in item and "Chainsaw" in item:
            chainsaw_charge = self.player.get_item_charges("Chainsaw")
            self.player.set_item_charges("Chainsaw", chainsaw_charge + 2)
            self.drop_item("Gasoline")
        else:
            print("These items cannot be used right now")
            return

    def choose_door(self, direction):
        if direction in self.chosen_tile.doors:
            print("Choose a NEW door not an existing one")
            return False
        else:
            self.chosen_tile.doors.append(direction)
            self.current_zombies = 3
            print(f"{self.current_zombies} Zombies have appeared, prepare for battle. Use the attack command to"
                  f" fight or the run command to flee")
            self.state = "Attacking"

    def search_for_totem(self):
        SearchForTotem.tile_action(self)

    def bury_totem(self):
        BuryTotem.tile_action(self)

    def check_for_dead_player(self):
        if self.player.health <= 0:
            return True
        else:
            return False

    @staticmethod
    def resolve_doors(n, e, s, w):
        doors = []
        if n == 1:
            doors.append(myD.NORTH)
        if e == 1:
            doors.append(myD.EAST)
        if s == 1:
            doors.append(myD.SOUTH)
        if w == 1:
            doors.append(myD.WEST)
        return doors

    def lose_game(self):
        self.state = "Game Over"

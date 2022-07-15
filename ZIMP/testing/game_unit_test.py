import unittest
from game import Game
from player import Player


class TestGameDefaults(unittest.TestCase):
    def setUp(self):
        self.game = Game(self)

    def test_self_player(self):
        self.assertTrue(self.game.player, 'player')

    def test_self_time(self):
        self.assertEqual(self.game.time, 9)

    def test_self_indoor_doors(self):
        self.assertEqual(self.game.indoor_tiles is None, False)

    def test_self_outdoor_doors(self):
        self.assertEqual(self.game.outdoor_tiles is None, False)

    def test_self_chosen_tile(self):
        self.assertEqual(self.game.chosen_tile is None, True)

    def test_self_dev_cards(self):
        self.assertEqual(self.game.dev_cards is None, False)

    def test_self_current_direction(self):
        self.assertEqual(self.game.current_move_direction is None, True)

    def test_can_cower(self):
        self.assertEqual(self.game.can_cower, True)

    def test_self_room_item(self):
        self.assertEqual(self.game.room_item is None, True)

    def test_indoor_tile_array(self):
        self.assertEqual(self.game.indoor_tiles, [])

    def test_outdoor_tile_array(self):
        self.assertEqual(self.game.outdoor_tiles, [])

    def test_dev_card_array(self):
        self.assertEqual(self.game.dev_cards, [])

    def test_defaults(self):
        game = Game(9, 'none', 'none', 'none', 'none', 'Starting', 'none', True)
        self.assertTrue(hasattr(game, 'time'))
        self.assertTrue(hasattr(game, 'indoor_tiles'))
        self.assertTrue(hasattr(game, 'outdoor_tiles'))
        self.assertTrue(hasattr(game, 'dev_cards'))
        self.assertTrue(hasattr(game, 'chosen_tile'))
        self.assertTrue(hasattr(game, 'state'))
        self.assertTrue(hasattr(game, 'current_move_direction'))
        self.assertTrue(hasattr(game, 'can_cower'))

    def tearDown(self):
        print("This test case is done!")


class TestGameStart(unittest.TestCase):
    def setUp(self):
        self.game = Game(self)

    def test_start(self):
        game = Game
        actual = game.start_game
        expected = game.start_game
        self.assertEqual(expected, actual)

    def test_state_starting(self):
        self.assertEqual(self.game.state, "Starting")

    def test_time_is_int(self):
        self.assertTrue(self.game.time.__int__())

    def test_starting_tile_name(self):
        actual = self.game.chosen_tile == 'Foyer'
        expected = self.game.chosen_tile == 'Foyer'
        self.assertEqual(expected, actual)

    def test_starting_tile_state(self):
        actual = self.game.state == 'Rotating'
        expected = self.game.state == 'Rotating'
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("This test case is done!")


class TestGetGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(self)

    def test_get_game(self):
        game = Game
        actual = game.get_game
        expected = game.get_game
        self.assertEqual(expected, actual)

    def test_tile_moving_state(self):
        actual = self.game.state == 'Moving'
        expected = self.game.state == 'Moving'
        self.assertEqual(expected, actual)

    def test_tile_rotating_state(self):
        actual = self.game.state == 'Rotating'
        expected = self.game.state == 'Rotating'
        self.assertEqual(expected, actual)

    def test_tile_choosing_state(self):
        actual = self.game.state == 'Choosing Door'
        expected = self.game.state == 'Choosing Door'
        self.assertEqual(expected, actual)

    def test_tile_drawing_state(self):
        actual = self.game.state == 'Drawing Dev Card'
        expected = self.game.state == 'Drawing Dev Card'
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("This test case is done!")


class TestPlayerStatus(unittest.TestCase):
    def setUp(self):
        self.game = Game(self)
        self.player = Player(self)

    def test_player_status(self):
        game = Game
        actual = game.get_player_status
        expected = game.get_player_status
        self.assertEqual(expected, actual)

    def test_time_status(self):
        actual = self.game.get_time()
        expected = self.game.get_time == 9
        self.assertFalse(expected, actual)

    def test_health_status(self):
        player = Player()
        actual = self.player.get_attack()
        expected = player.health == 6
        self.assertTrue(expected, actual)

    def test_attack_status(self):
        player = Player()
        actual = self.player.get_attack()
        expected = player.attack == 1
        self.assertTrue(expected, actual)

    def tearDown(self):
        print("This test case is done!")

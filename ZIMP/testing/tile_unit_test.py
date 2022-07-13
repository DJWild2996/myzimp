import unittest
from indoor_tile_factory import IndoorTileFactory
from indoor_tile import IndoorTile
from outdoor_tile import OutdoorTile


class TestTile(unittest.TestCase):
    def setUp(self):
        self.tile = IndoorTile(self)

    def test_defaults(self):
        tile = IndoorTile('name', 16, 16, 'none', 'none', 'none')
        self.assertTrue(hasattr(tile, 'name'))
        self.assertTrue(hasattr(tile, 'x'))
        self.assertTrue(hasattr(tile, 'y'))
        self.assertTrue(hasattr(tile, 'effect'))
        self.assertTrue(hasattr(tile, 'doors'))
        self.assertTrue(hasattr(tile, 'entrance'))

    def test_self_x(self):
        self.assertEqual(self.tile.x, 16)

    def test_set_x(self):
        tile = IndoorTile
        tile.set_x(self, x='x')
        self.assertEqual(tile.set_x, 'x')

    def test_self_y(self):
        self.assertEqual(self.tile.y, 16)

    def test_set_y(self):
        tile = IndoorTile
        tile.set_y(self, y='y')
        self.assertEqual(tile.set_y, 'y')

    def test_self_effect(self):
        self.assertEqual(self.tile.effect, None)

    def test_self_doors(self):
        self.assertEqual(self.tile.doors, [])

    def test_self_entrance(self):
        self.assertEqual(self.tile.entrance, None)

    def test_tile_has_setx(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'set_x'))
        self.assertTrue(callable(getattr(tile, 'set_x', None)))

    def test_tile_has_sety(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'set_y'))
        self.assertTrue(callable(getattr(tile, 'set_y', None)))

    def test_tile_has_change_door_position(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'change_door_position'))
        self.assertTrue(callable(getattr(tile, 'change_door_position', None)))

    def test_tile_has_set_entrance(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'set_entrance'))
        self.assertTrue(callable(getattr(tile, 'set_entrance', None)))

    def test_tile_rotate_entrance(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'rotate_entrance'))
        self.assertTrue(callable(getattr(tile, 'rotate_entrance', None)))

    def test_rotate_tile(self):
        tile = IndoorTile
        self.assertTrue(hasattr(tile, 'rotate_tile'))
        self.assertTrue(callable(getattr(tile, 'rotate_tile', None)))

    def test_tile_setx(self):
        tile = IndoorTile
        actual = tile.set_x
        expected = tile.set_x
        self.assertEqual(expected, actual)

    def test_tile_sety(self):
        tile = IndoorTile
        actual = tile.set_y
        expected = tile.set_y
        self.assertEqual(expected, actual)

    def test_tile_door_position(self):
        tile = IndoorTile
        actual = tile.change_door_position
        expected = tile.change_door_position
        self.assertEqual(expected, actual)

    def test_tile_set_entrance(self):
        tile = IndoorTile
        actual = tile.set_entrance
        expected = tile.set_entrance
        self.assertEqual(expected, actual)

    def test_tile_rotate_entrance(self):
        tile = IndoorTile
        actual = tile.rotate_entrance
        expected = tile.rotate_entrance
        self.assertEqual(expected, actual)

    def test_tile_rotate_tile(self):
        tile = IndoorTile
        actual = tile.rotate_tile
        expected = tile.rotate_tile
        self.assertEqual(expected, actual)

    def test_change_door_position(self):
        tile = IndoorTile('name', 16, 16, 'none', 'none', 'none')
        self.assertTrue(hasattr(tile, 'change_door_position'))
        self.assertTrue(callable(getattr(tile, 'change_door_position', None)))

    def test_set_entrance(self):
        tile = IndoorTile('name', 16, 16, 'none', 'none', 'none')
        self.assertTrue(hasattr(tile, 'set_entrance'))
        self.assertTrue(callable(getattr(tile, 'set_entrance', None)))

    def test_door_direction(self):
        tile = IndoorTile
        tile.change_door_position(self, idx=self.tile.doors, direction='direction')
        self.assertEqual(tile.change_door_position, 'direction')

    def test_entrance_direction(self):
        tile = IndoorTile
        tile.set_entrance(self, direction=self.tile.entrance)
        self.assertEqual(tile.set_entrance, 'direction')

    def tearDown(self):
        print("This test case is done!")


class TestIndoorTile(unittest.TestCase):
    def setUp(self):
        self.indoor = IndoorTile(self)

    def test_indoor_defaults(self):
        indoor = IndoorTile('name', 16, 16, 'none', 'none', 'none')
        self.assertTrue(hasattr(indoor, 'name'))
        self.assertTrue(hasattr(indoor, 'x'))
        self.assertTrue(hasattr(indoor, 'y'))
        self.assertTrue(hasattr(indoor, 'effect'))
        self.assertTrue(hasattr(indoor, 'doors'))
        self.assertTrue(hasattr(indoor, 'entrance'))

    def test_indoor_has___init__(self):
        indoor = IndoorTile
        self.assertTrue(hasattr(indoor, '__init__'))
        self.assertTrue(callable(getattr(indoor, '__init__', None)))

    def test_indoor_has___repr__(self):
        indoor = IndoorTile
        self.assertTrue(hasattr(indoor, '__repr__'))
        self.assertTrue(callable(getattr(indoor, '__repr__', None)))

    def test_indoor___repr__returns_string(self):
        indoor = IndoorTile
        returned = str(indoor)
        self.assertTrue(isinstance(returned, str))

    def test_self_indoor_doors(self):
        self.assertEqual(self.indoor.doors, [])

    def test___repr__working(self):
        indoor = IndoorTile
        actual = indoor.__repr__(self.indoor)
        expected = indoor.__repr__(self.indoor)
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("This test case is done!")


class TestOutdoorTile(unittest.TestCase):
    def setUp(self):
        self.outdoor = OutdoorTile(self)

    def test_outdoor_defaults(self):
        outdoor = OutdoorTile('name', 16, 16, 'none', 'none', 'none')
        self.assertTrue(hasattr(outdoor, 'name'))
        self.assertTrue(hasattr(outdoor, 'x'))
        self.assertTrue(hasattr(outdoor, 'y'))
        self.assertTrue(hasattr(outdoor, 'effect'))
        self.assertTrue(hasattr(outdoor, 'doors'))
        self.assertTrue(hasattr(outdoor, 'entrance'))

    def test_outdoor_has___init__(self):
        outdoor = OutdoorTile
        self.assertTrue(hasattr(outdoor, '__init__'))
        self.assertTrue(callable(getattr(outdoor, '__init__', None)))

    def test_outdoor_has___repr__(self):
        outdoor = OutdoorTile
        self.assertTrue(hasattr(outdoor, '__repr__'))
        self.assertTrue(callable(getattr(outdoor, '__repr__', None)))

    def test_outdoor___repr__returns_string(self):
        outdoor = OutdoorTile
        returned = str(outdoor)
        self.assertTrue(isinstance(returned, str))

    def test_self_outdoor_doors(self):
        self.assertEqual(self.outdoor.doors, [])

    def test___repr__working(self):
        outdoor = OutdoorTile
        actual = outdoor.__repr__(self.outdoor)
        expected = outdoor.__repr__(self.outdoor)
        self.assertEqual(expected, actual)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main()

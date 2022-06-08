import unittest

from abstract_factory import BaseAbstractFactory


class TestTile(unittest.TestCase):

    def test_abstract_factory_setx(self):
        factory = BaseAbstractFactory
        actual = factory.set_x
        expected = factory.set_x
        self.assertEqual(expected, actual)

    def test_abstract_factory_sety(self):
        factory = BaseAbstractFactory
        actual = factory.set_y
        expected = factory.set_y
        self.assertEqual(expected, actual)

    def test_abstract_factory_door_position(self):
        factory = BaseAbstractFactory
        actual = factory.change_door_position
        expected = factory.change_door_position
        self.assertEqual(expected, actual)

    def test_abstract_factory_set_entrance(self):
        factory = BaseAbstractFactory
        actual = factory.set_entrance
        expected = factory.set_entrance
        self.assertEqual(expected, actual)

    def test_abstract_factory_rotate_entrance(self):
        factory = BaseAbstractFactory
        actual = factory.rotate_entrance
        expected = factory.rotate_entrance
        self.assertEqual(expected, actual)

    def test_abstract_factory_rotate_tile(self):
        factory = BaseAbstractFactory
        actual = factory.rotate_tile
        expected = factory.rotate_tile
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

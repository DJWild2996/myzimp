import unittest
from game import Game


class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(self)

    def tearDown(self):
        print("This test case is done!")


if __name__ == '__main__':
    unittest.main()

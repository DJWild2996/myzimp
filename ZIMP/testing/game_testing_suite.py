from game_unit_test import TestGameDefaults
from game_unit_test import TestGameStart
from game_unit_test import TestGetGame
from game_unit_test import TestPlayerStatus

import unittest


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestGameDefaults))
    the_suite.addTest(unittest.makeSuite(TestGameStart))
    the_suite.addTest(unittest.makeSuite(TestGetGame))
    the_suite.addTest(unittest.makeSuite(TestPlayerStatus))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)

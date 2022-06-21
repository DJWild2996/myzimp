from tile_unit_test import TestTile
from tile_unit_test import TestIndoorTile
from tile_unit_test import TestOutdoorTile

import unittest


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestTile))
    the_suite.addTest(unittest.makeSuite(TestIndoorTile))
    the_suite.addTest(unittest.makeSuite(TestOutdoorTile))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)

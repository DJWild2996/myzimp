from game_unit_test import TestGame

import unittest


def suite():
    the_suite = unittest.TestSuite()
    the_suite.addTest(unittest.makeSuite(TestGame))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)

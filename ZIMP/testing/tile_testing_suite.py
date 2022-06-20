from TileUnitTest import TestTile

import unittest


def suite():
    the_suite = unittest.TestSuite()
    '''
    suite1.addTest(TestTile("test_abstract_factory_setx"))
    suite1.addTest(TestTile("test_abstract_factory_sety"))
    suite1.addTest(TestTile("test_abstract_factory_door_position"))
    suite1.addTest(TestTile("test_abstract_factory_set_entrance"))
    suite1.addTest(TestTile("test_abstract_factory_rotate_entrance"))
    suite1.addTest(TestTile("test_abstract_factory_rotate_tile"))
    '''
    the_suite.addTest(unittest.makeSuite(TestTile))
    return the_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    test_suite = suite()
    runner.run(test_suite)

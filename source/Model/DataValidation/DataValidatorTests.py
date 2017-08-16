import unittest
from Model.DataValidator.DataValidator import *

class DataValidatorTests(unittest.TestCase):

    def setUpClass(cls):
        # sets up class once

    def setUp(self):
        # be executed before each test
        self.x = 5

    def tearDown(self):
        # be executed after each test case
        print('down')

    def test_01(self):
        self.assertTrue(self.x == 5, "the value of x should be 5!")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
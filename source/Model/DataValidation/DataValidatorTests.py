import unittest
from DataValidator import *


class DataValidatorTests(unittest.TestCase):

    def setUp(self):
        # be executed before each test
        print("set up")

    def tearDown(self):
        # be executed after each test case
        print("teardown")

    def test_01(self):
        x = 5
        self.assertTrue(x == 5, "the value of x should be 5!")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()
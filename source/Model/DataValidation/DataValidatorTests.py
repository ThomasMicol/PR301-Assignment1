import unittest
from DataValidator import *


class DataValidatorTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dataValidator = DataValidator()

    def setUp(self):
        # be executed before each test
        print("set up")
        self.data = [['A001', 'F', '23', '456', 'Normal', '23', '30-5-1994'],
                     ['C234', 'M', '5', '676', 'Overweight', '300', '1-12-1977'],
                     ['C4', 'Male', 'nine', '66,8', 'heavy', '3,00', '1-12-19']]

    def tearDown(self):
        # be executed after each test case
        print("teardown")

    def test_person_age_01(self):
        # good day test for person 1
        age = self.data[0][2]
        self.assertTrue(self.dataValidator.validate_age(age), "That is not a valid age input")

    def test_person_age_02(self):
        # good day test for person 2
        age = self.data[1][2]
        self.assertTrue(self.dataValidator.validate_age(age), "That is not a valid age input")

    def test_person_age_03(self):
        # bad day test for person 3 bad data is rejected
        age = self.data[2][2]
        self.assertFalse(self.dataValidator.validate_age(age), "That is not a valid age input")


if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()

import unittest
from Model.Database.Database import *

class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.database_handler = Database()

    def tearDown(self):
        self.database_handler = None

    def test_01(self):
        # TODO I left this blank because i didnt have time
        # implement it
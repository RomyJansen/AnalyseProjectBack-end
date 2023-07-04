import unittest

from app.Data.VariabelenDataHandler import VariabelenDataHandler


class TestVariabelenDataHandler(unittest.TestCase):

    sut = VariabelenDataHandler()

    def set_up(self):
        self.sut = VariabelenDataHandler()

    def test_get_item_from_id_returns_correct(self):
        print(self.sut.get_variabele_waarde_from_id(3))

        self.assertEqual(True, True)
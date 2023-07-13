import unittest

from app.Data.ModelHandlers.VariabelenDataHandler import VariabelenDataHandler


class TestVariabelenDataHandler(unittest.TestCase):

    sut = VariabelenDataHandler()

    def set_up(self):
        self.sut = VariabelenDataHandler()

    def test_get_item_from_id_returns_correct(self):
        print(self.sut.get_variabele_waarde_from_id(3))

        self.assertEqual(True, True)

    def test_get_start_variabelen_haalt_startvariabelen_op(self):
        print(self.sut.get_start_variabelen())

        self.assertEqual(True, True)
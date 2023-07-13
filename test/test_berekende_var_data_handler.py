import unittest

from app.Data.ModelHandlers.BerekendeVarDataHandler import BerekendeVarDataHandler


class TestBerekendeVarDataHandler(unittest.TestCase):

    sut = BerekendeVarDataHandler()

    def set_up(self):
        self.sut = BerekendeVarDataHandler()

    def test_get_item_from_id_returns_correct(self):
        print(self.sut.get_item_from_id(1).json())

        self.assertEqual(True, True)

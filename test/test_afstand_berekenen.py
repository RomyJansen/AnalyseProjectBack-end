import unittest
from unittest import mock

from app.AnalyseComponent.AfstandBerekenen import AfstandBerekenen


class TestAfstandBerekenen(unittest.TestCase):

    sut = AfstandBerekenen()

    def set_up(self):
        self.sut = AfstandBerekenen()

    def test_optelberekening_wordt_correct_uitgevoerd(self):
        self.assertEquals(self.sut._bereken_afstand(60, 50, 250, 50), 190)


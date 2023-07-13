import unittest
from unittest import mock

from app.AnalyseComponent.Berekenen import Berekenen


class TestBerekenen(unittest.TestCase):

    sut = Berekenen()

    def set_up(self):
        self.sut = Berekenen()

    def test_optelberekening_wordt_correct_uitgevoerd(self):
        self.assertEqual(self.sut._doe_berekening(4, 5, "+"), 9)

    def test_aftelberekening_wordt_correct_uitgevoerd(self):
        self.assertEqual(self.sut._doe_berekening(4, 5, "-"), -1)

    def test_vermenigvuldigberekening_wordt_correct_uitgevoerd(self):
        self.assertEqual(self.sut._doe_berekening(4, 5, "*"), 20)

    def test_deelberekening_wordt_correct_uitgevoerd(self):
        self.assertEqual(self.sut._doe_berekening(4, 5, "/"), 0.8)

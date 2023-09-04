from unittest import TestCase, mock

from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Models.AfstandVar import AfstandVar
from app.Models.Object import Object


class TestAfstandBerekenen(TestCase):
    sut = AfstandBerekenen()
    testAfstandVar: AfstandVar = AfstandVar(id=1, naam="afstand1", doelObjectType=2, waarde=0, jaar=2023, objectLink=1, results=[])
    testObject: Object = Object(id=2, naam="test2", objectType=2)
    testObjectList: list = [Object(id=1, naam="test1", objectType=1), testObject, Object(id=3, naam="test3", objectType=1)]

    def set_up(self):
        self.sut = AfstandBerekenen()

    @mock.patch.object(AfstandBerekenen, '_find_specific_object', return_value=testObject)
    @mock.patch.object(AfstandBerekenen, '_bereken_afstand', return_value=0)
    def test_bereken_afstand_voor_item_returns_correct_results(self, mock__find_specific_object, mock__bereken_afstand):
        self.assertEqual(self.sut.bereken_afstand_voor_item(self.testAfstandVar, self.testObjectList).pop().naam, self.testObject.naam)

    def test_find_specific_object_returns_correct_object(self):
        self.assertEqual(self.sut._find_specific_object(self.testObjectList, self.testObject.id).naam, self.testObject.naam)

    def test_find_specific_object_throws_error_with_empty_list(self):
        objectList: list = []
        self.assertRaises(TypeError, self.sut._find_specific_object(objectList, 1))

    def test_bereken_afstand_returns_correct_answer(self):
        self.assertEqual(self.sut._bereken_afstand(60, 50, 250, 50), 190)

    def test_bereken_afstand_returns_correct_answer_when_negative_values_used(self):
        self.assertEqual(round(self.sut._bereken_afstand(-60, 50, 250, -50)), 326)

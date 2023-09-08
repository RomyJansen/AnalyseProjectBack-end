from unittest import TestCase, mock

from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Data.ModelHandlers.AfstandVarDataHandler import AfstandVarDataHandler
from app.Data.ModelHandlers.ObjectDataHandler import ObjectDataHandler
from app.Models.AfstandVar import AfstandVar
from app.Models.Object import Object
from app.Models.Variabele import Variabele


class TestAfstandBerekenen(TestCase):
    sut = AfstandBerekenen()
    testAfstandVar: AfstandVar = AfstandVar(id=1, naam="afstand1", doelObjectType=2, waarde=0, jaar=2023, objectLink=1,
                                            results=[])
    testObject: Object = Object(id=2, naam="test2", objectType=2)
    testObjectList: list = [Object(id=1, naam="test1", objectType=1), testObject,
                            Object(id=3, naam="test3", objectType=1)]
    testVar: Variabele = Variabele(id=5, naam="var5", waarde=0, jaar=0)

    @mock.patch.object(AfstandVarDataHandler, 'get_all_from_db', return_value=[testAfstandVar])
    @mock.patch.object(ObjectDataHandler, 'get_all_from_db', return_value=testObjectList)
    @mock.patch.object(AfstandBerekenen, 'bereken_afstand_voor_item', return_value=[testVar])
    def test_bereken_alle_afstanden_returns_correct_result(self, mock_get_all_from_db_afstand,
                                                           mock_get_all_from_db_object, mock_bereken_afstand_voor_item):
        self.testAfstandVar.results.append(self.testVar)
        self.assertEqual(self.sut.bereken_alle_afstanden(), [self.testAfstandVar])

    @mock.patch.object(AfstandVarDataHandler, 'get_all_from_db', return_value=[])
    @mock.patch.object(ObjectDataHandler, 'get_all_from_db', return_value=[])
    @mock.patch.object(AfstandBerekenen, 'bereken_afstand_voor_item', return_value=[])
    def test_bereken_alle_afstanden_raises_error_for_empty_var_list(self, mock_get_all_from_db_afstand,
                                                                    mock_get_all_from_db_object,
                                                                    mock_bereken_afstand_voor_item):
        self.assertRaises(TypeError, self.sut.bereken_alle_afstanden())

    @mock.patch.object(AfstandVarDataHandler, 'get_all_items_from_year', return_value=[testAfstandVar])
    @mock.patch.object(ObjectDataHandler, 'get_all_items_from_year', return_value=testObjectList)
    @mock.patch.object(AfstandBerekenen, 'bereken_afstand_voor_item', return_value=[testVar])
    def test_bereken_alle_afstanden_voor_jaar_returns_correct_results(self, mock_get_all_items_from_year_afstand,
                                                                      mock_get_all_items_from_year_objects,
                                                                      mock_bereken_afstand_voor_item):
        self.testAfstandVar.results.append(self.testVar)
        self.assertEqual(self.sut.bereken_alle_afstanden_voor_jaar(0), [self.testAfstandVar])

    @mock.patch.object(AfstandVarDataHandler, 'get_all_items_from_year', return_value=[])
    @mock.patch.object(ObjectDataHandler, "get_all_items_from_year", return_value=[])
    @mock.patch.object(AfstandBerekenen, 'bereken_afstand_voor_item', return_value=[])
    def test_bereken_alle_afstanden_voor_jaar_raises_error_for_empty_var_list(self,
                                                                              mock_get_all_items_from_year_objects,
                                                                              mock_get_all_items_from_year_afstandvar,
                                                                              mock_bereken_afstand_voor_item):
        self.assertRaises(TypeError, self.sut.bereken_alle_afstanden_voor_jaar(0))

    @mock.patch.object(AfstandBerekenen, '_find_specific_object', return_value=testObject)
    @mock.patch.object(AfstandBerekenen, '_bereken_afstand', return_value=0)
    def test_bereken_afstand_voor_item_returns_correct_results(self, mock__find_specific_object, mock__bereken_afstand):
        self.assertEqual(self.sut.bereken_afstand_voor_item(self.testAfstandVar, self.testObjectList).pop().naam,
                         self.testObject.naam)

    @mock.patch.object(AfstandBerekenen, '_find_specific_object', return_value=testObject)
    @mock.patch.object(AfstandBerekenen, '_bereken_afstand', return_value=0)
    def test_bereken_afstand_voor_item_returns_empty_list(self, mock__find_specific_object, mock__bereken_afstand):
        self.assertEqual(self.sut.bereken_afstand_voor_item(self.testAfstandVar, []), [])

    def test_find_specific_object_returns_correct_object(self):
        self.assertEqual(self.sut._find_specific_object(self.testObjectList, self.testObject.id).naam,
                         self.testObject.naam)

    def test_find_specific_object_throws_error_with_empty_list(self):
        objectList: list = []
        self.assertRaises(TypeError, self.sut._find_specific_object(objectList, 1))

    def test_bereken_afstand_returns_correct_answer(self):
        self.assertEqual(self.sut._bereken_afstand(60, 50, 250, 50), 190)

    def test_bereken_afstand_returns_correct_answer_when_negative_values_used(self):
        self.assertEqual(round(self.sut._bereken_afstand(-60, 50, 250, -50)), 326)

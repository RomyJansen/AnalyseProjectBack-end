from app.Data.DataHandler import DataHandler
from app.Models.Gebeurtenis import Gebeurtenis, ObjectGebeurtenis


class GebeurtenisDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_alle_gebeurtenissen(self):
        alle_gebeurtenissen: list = [self.get_objects_from_db(), self.get_object_gebeurtenissen()]
        return alle_gebeurtenissen

    def get_objects_from_db(self):
        query = "SELECT * FROM Gebeurtenissen"
        results = self._data_handler.get_items_from_db(query, ())
        gebeurtenissen = []
        for result in results:
            gebeurtenissen.append(self._put_result_into_gebeurtenis(result))

        return gebeurtenissen

    def _put_result_into_gebeurtenis(self, result):
        gebeurtenis_info = Gebeurtenis()

        gebeurtenis_info.id = result[0]
        gebeurtenis_info.naam = result[1]
        gebeurtenis_info.jaar = result[2]
        gebeurtenis_info.waarde = result[3]

        return gebeurtenis_info

    def add_gebeurtenis_to_db(self, gebeurtenis: Gebeurtenis):
        query = "INSERT INTO gebeurtenissen (id, naam, jaar, waarde) VALUE (%s, %s, %s , %s)"
        self._data_handler.add_item_to_db(query,
                                          (gebeurtenis.id, gebeurtenis.naam, gebeurtenis.jaar, gebeurtenis.waarde))

    def get_object_gebeurtenissen(self):
        query = "SELECT * FROM objectGebeurtenissen"
        results = self._data_handler.get_items_from_db(query, ())
        gebeurtenissen = []
        for result in results:
            gebeurtenissen.append(self._put_result_into_gebeurtenis(result))

        return gebeurtenissen

    def _put_result_into_objectGebeurtenis(self, result):
        gebeurtenis_info = ObjectGebeurtenis()

        gebeurtenis_info.id = result[0]
        gebeurtenis_info.naam = result[1]
        gebeurtenis_info.jaar = result[2]
        gebeurtenis_info.locatieX = result[3]
        gebeurtenis_info.locatieY = result[4]

        return gebeurtenis_info

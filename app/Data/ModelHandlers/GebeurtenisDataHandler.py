from app.Data.DataHandler import DataHandler
from app.Models.Gebeurtenis import Gebeurtenis


class GebeurtenisDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_objects_from_db(self):
        query = "SELECT * FROM Gebeurtenissen"
        results = self._data_handler.get_items_from_db(query, ())
        gebeurtenissen = []
        for result in results:
            gebeurtenissen.append(self._put_result_into_gebeurtenis(result))

        return gebeurtenissen

    def _put_result_into_gebeurtenis(self, result):
        gebeurtenisInfo = Gebeurtenis()

        gebeurtenisInfo.id = result[0]
        gebeurtenisInfo.naam = result[1]
        gebeurtenisInfo.jaar = result[2]
        gebeurtenisInfo.waarde = result[3]

        return gebeurtenisInfo

    def add_gebeurtenis_to_db(self, gebeurtenis: Gebeurtenis):
        query = "INSERT INTO gebeurtenissen (id, naam, jaar, waarde) VALUE (%s, %s, %s , %s)"
        self._data_handler.add_item_to_db(query, (gebeurtenis.id, gebeurtenis.naam, gebeurtenis.jaar, gebeurtenis.waarde))

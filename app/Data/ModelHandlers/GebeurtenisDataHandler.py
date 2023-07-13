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
        gebeurtenisInfo.varId = result[2]
        gebeurtenisInfo.jaar = result[3]
        gebeurtenisInfo.waarde = result[4]

        return gebeurtenisInfo

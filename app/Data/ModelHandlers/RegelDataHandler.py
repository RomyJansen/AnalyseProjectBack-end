from app.Data.DataHandler import DataHandler
from app.Models.Regel import Regel


class RegelDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_objects_from_db(self):
        query = "SELECT * FROM Regels"
        results = self._data_handler.get_items_from_db(query, ())
        regels = []
        for result in results:
            regels.append(self._put_result_into_regel(result))

        return regels

    def _put_result_into_regel(self, result):
        regelInfo = Regel()

        regelInfo.id = result[0]
        regelInfo.naam = result[1]
        regelInfo.waarde = result[2]
        regelInfo.vergelijkingOperator = result[3]
        regelInfo.varId = result[4]

        return regelInfo

from app.Data.DataHandler import DataHandler
from app.Business.IModelDataHandler import IModelDataHandler
from app.Models.Regel import Regel


class RegelDataHandler(IModelDataHandler):
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_all_from_db(self):
        query = "SELECT * FROM regels"
        results = self._data_handler.get_items_from_db(query, ())
        regels = []
        for result in results:
            regels.append(self._put_result_into_object(result))

        return regels

    def get_item_from_id(self, id: int):
        query = "SELECT * FROM regels WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_result_into_object(results[0])

    def _put_result_into_object(self, result):
        regelInfo = Regel()

        regelInfo.id = result[0]
        regelInfo.naam = result[1]
        regelInfo.waarde = result[2]
        regelInfo.vergelijkingOperator = result[3]
        regelInfo.varId = result[4]
        regelInfo.results = []

        return regelInfo

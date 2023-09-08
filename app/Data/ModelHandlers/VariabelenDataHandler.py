from app.Data.DataHandler import DataHandler
from app.Business.IModelDataHandler import IModelDataHandler
from app.Models.Variabele import Variabele, VariabeleKoppeling


class VariabelenDataHandler(IModelDataHandler):
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    # def get_variabele_waarde_from_id(self, id: int):
    #     result = self.get_koppeling_from_id(id)
    #     if result.typeId == 2:
    #         return self.

    def get_koppeling_from_id(self, id: int):
        query = "SELECT * FROM AlleVariabelen WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_koppeling_into_object(results[0])

    def get_all_koppeling_from_db(self):
        query = "SELECT * FROM alleVariabelen"
        results = self._data_handler.get_items_from_db(query, ())
        varList = []
        for row in results:
            varList.append(self._put_koppeling_into_object(row))

        return varList

    def get_item_from_id(self, id: int):
        query = "SELECT * FROM standaardVariabelen WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_result_into_object(results[0])

    def get_all_from_db(self):
        query = "SELECT * FROM StandaardVariabelen"
        results = self._data_handler.get_items_from_db(query, ())
        varList = []
        for row in results:
            varList.append(self._put_result_into_object(row))

        return varList

    def _put_result_into_object(self, result: []):
        varInfo = Variabele(id=1, naam="test", waarde=0, jaar=0)

        varInfo.id = result[0]
        varInfo.waarde = result[1]

        return varInfo

    def _put_koppeling_into_object(self, result: []):
        varInfo = VariabeleKoppeling(id=0, typeId=0, varId=0, objectLink=0)

        varInfo.id = result[0]
        varInfo.typeId = result[1]
        varInfo.varId = result[varInfo.typeId + 1]
        varInfo.objectLink = result[5]

        return varInfo

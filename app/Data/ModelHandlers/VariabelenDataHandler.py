from app.Data.DataHandler import DataHandler
from app.Models.Variabele import Variabele


class VariabelenDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_variabele_waarde_from_id(self, id: int):
        return self.get_variabele_from_id(id).waarde

    def get_variabele_from_id(self, id: int):
        query = "SELECT * FROM AlleVariabelen WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_result_var_into_object(results[0])

    def get_start_variabelen(self):
        query = "SELECT * FROM StartVariabelen"
        results = self._data_handler.get_items_from_db(query, ())
        varList = []
        for row in results:
            varList.append(self._put_result_var_into_object(row))

        return varList

    def _put_result_var_into_object(self, result: []):
        varInfo = Variabele(id=1, naam="test", waarde=0)

        varInfo.id = result[0]
        varInfo.waarde = result[1]

        return varInfo
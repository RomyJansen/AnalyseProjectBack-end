from app.Data.DataHandler import DataHandler
from app.Models.AfstandVar import AfstandVar

from app.Models.BerekendeVar import BerekendeVar


class AfstandVarDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_item_from_id(self, id: int):
        query = "SELECT * FROM afstandVariabelen WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_result_berekende_var_into_object(results[0])

    def get_all_bv_from_db(self):
        query = "SELECT * FROM afstandVariabelen"
        results = self._data_handler.get_items_from_db(query, ())
        bv_list = []
        for row in results:
            bv_list.append(self._put_result_berekende_var_into_object(row))

        return bv_list

    def _put_result_berekende_var_into_object(self, result: []):
        varInfo = AfstandVar(id=1, naam="test", waarde=0, objectLink=0, doelObjectType=0, results=[])

        varInfo.id = result[0]
        varInfo.naam = result[1]
        varInfo.objectLink = result[2]
        varInfo.doelObjectType = result[3]

        return varInfo

    def get_all_object_types(self):
        query = "SELECT * FROM objectTypes"
        results = self._data_handler.get_items_from_db(query, ())
        bv_list = []
        for row in results:
            bv_list.append(self._put_objecttype_into_model(row))

        return bv_list

    def _put_objecttype_into_model(self, result: []):
        typeInfo = ObjectType(id=0, naam="test", results=[])

        typeInfo.id = result[0]
        typeInfo.naam = result[1]

        return typeInfo

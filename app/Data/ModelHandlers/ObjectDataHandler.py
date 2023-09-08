from app.Data.DataHandler import DataHandler
from app.Business.IModelDataHandler import IModelDataHandler
from app.Models.Object import Object


class ObjectDataHandler(IModelDataHandler):
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_all_items_from_year(self, jaar: int):
        query = "SELECT * FROM objecten WHERE (id, jaar) IN (SELECT id, MAX(jaar) as jaar FROM objecten WHERE jaar < %s group by id)"
        results = self._data_handler.get_items_from_db(query, (jaar,))
        obj_list = []
        for row in results:
            obj_list.append(self._put_result_into_object(row))

        return obj_list

    def get_item_from_id(self, id: int):
        query = "SELECT * FROM objecten WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        obj_list = []
        for row in results:
            obj_list.append(self._put_result_into_object(row))

        return obj_list


    def get_all_from_db(self):
        query = "SELECT * FROM Objecten"
        results = self._data_handler.get_items_from_db(query, ())
        objects = []
        for result in results:
            objects.append(self._put_result_into_object(result))

        return objects

    def _put_result_into_object(self, result):
        objectInfo = Object(id=1, naam="test", waarde=0)

        objectInfo.id = result[0]
        objectInfo.naam = result[1]
        objectInfo.objectType = result[2]
        objectInfo.locatieX = result[3]
        objectInfo.locatieY = result[4]
        objectInfo.grootteX = result[5]
        objectInfo.grootteY = result[6]
        objectInfo.jaar = result[7]

        return objectInfo

if __name__ == '__main__':
    handler = ObjectDataHandler()
    print(handler.get_all_items_from_year(2028))
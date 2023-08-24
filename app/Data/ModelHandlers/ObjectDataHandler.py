from app.Data.DataHandler import DataHandler
from app.Models.Object import Object


class ObjectDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_objects_from_db(self):
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

        return objectInfo
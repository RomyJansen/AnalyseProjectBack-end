from app.Data.DataHandler import DataHandler


class ObjectDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_objects_from_db(self):
        query = "SELECT * FROM Object"
        results = self._data_handler.get_items_from_db(query, ())


    def _put_result_into_object(self):

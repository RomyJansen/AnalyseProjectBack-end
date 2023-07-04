from app.Data.DataHandler import DataHandler

from app.Models.BerekendeVar import BerekendeVar


class BerekendeVarDataHandler:
    _data_handler: DataHandler

    def __init__(self):
        self._data_handler = DataHandler()

    def get_item_from_id(self, id: int):
        query = "SELECT * FROM BerekendeVariabelen WHERE id = %s"
        results = self._data_handler.get_items_from_db(query, (id,))
        return self._put_result_berekende_var_into_object(results[0])

    def _put_result_berekende_var_into_object(self, result: []):
        varInfo = BerekendeVar(id=1, naam="test", waarde=0, var1Id=0, var2Id=0, object1Id=0, object2Id=0, operator="+",
                               objectBerekening=False,)

        varInfo.id = result[0]
        varInfo.naam = result[1]
        if result[6] > 0:
            varInfo.objectBerekening = True
            varInfo.object1Id = result[2]
            varInfo.object2Id = result[3]
        else:
            varInfo.objectBerekening = False
            varInfo.var1Id = result[2]
            varInfo.var2Id = result[3]
        varInfo.operator = result[4]
        varInfo.waarde = result[5]

        return varInfo
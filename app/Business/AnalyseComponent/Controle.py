from app.Data.ModelHandlers.RegelDataHandler import RegelDataHandler
from app.Data.ModelHandlers.VariabelenDataHandler import VariabelenDataHandler


class Controle:
    _var_data_handler: VariabelenDataHandler
    _regel_data_handler: RegelDataHandler
    _regels: list

    def __init__(self):
        self._var_data_handler = VariabelenDataHandler()
        self._regel_data_handler = RegelDataHandler()
        self._regels = self._regel_data_handler.get_all_from_db()

    # rekening houdem met regels rondom gebeurtenissen!

    def controleer_alle_regels(self):
        for regel in self._regels:
            regel.results.append({regel.id, self._controleer_regel(regel)})
        return self._regels

    def _controleer_regel(self, regel):
        waarde1 = self._var_data_handler.get_variabele_waarde_from_id(regel.varId)
        waarde2 = regel.waarde
        if regel.vergelijkingOperator == ">":
            if waarde1 > waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "<":
            if waarde1 < waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "=":
            if waarde1 == waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == ">=":
            if waarde1 >= waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "<=":
            if waarde1 <= waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "!=":
            if waarde1 != waarde2:
                return True
            else:
                return False
        else:
            return False

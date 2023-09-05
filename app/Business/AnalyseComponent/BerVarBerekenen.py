from typing import List

from app.Business.IModelDataHandler import IModelDataHandler
from app.Data.ModelHandlers.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.ModelHandlers.VariabelenDataHandler import VariabelenDataHandler
from app.Models.BerekendeVar import BerekendeVar


class BerVarBerekenen:
    berekende_var_data_handler: IModelDataHandler = BerekendeVarDataHandler()
    variabelen_data_handler: IModelDataHandler = VariabelenDataHandler()

    def bereken_alle_berekende_var(self):
        berekende_vars: List[BerekendeVar] = self.berekende_var_data_handler.get_all_from_db()
        for var in berekende_vars:
            var.results.append(self.bereken_berekende_var(var.id))
        return berekende_vars

    def bereken_berekende_var(self, varId):
        nieuweWaarde: int
        var = self.berekende_var_data_handler.get_item_from_id(varId)
        if var.objectBerekening:
            nieuweWaarde = self._doe_object_berekening(var)
        else:
            nieuweWaarde = self._doe_var_berekening(var)

        return nieuweWaarde

    def _doe_object_berekening(self, var: BerekendeVar):
        return 0

    def _doe_var_berekening(self, var: BerekendeVar):
        var1Waarde = self.variabelen_data_handler.get_variabele_waarde_from_id(var.var1Id)
        var2Waarde = self.variabelen_data_handler.get_variabele_waarde_from_id(var.var2Id)
        return self._doe_berekening(var1Waarde, var2Waarde, var.operator)

    def _doe_berekening(self, value1: int, value2: int, operator):
        if operator == "+":
            return value1 + value2
        elif operator == "-":
            return value1 - value2
        elif operator == "*":
            return value1 * value2
        else:
            return value1 / value2

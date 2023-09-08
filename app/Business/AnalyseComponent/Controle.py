from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Business.IModelDataHandler import IModelDataHandler
from app.Data.ModelHandlers.AfstandVarDataHandler import AfstandVarDataHandler
from app.Data.ModelHandlers.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.ModelHandlers.RegelDataHandler import RegelDataHandler
from app.Data.ModelHandlers.VariabelenDataHandler import VariabelenDataHandler


class Controle:
    _var_data_handler: IModelDataHandler
    _ber_var_data_handler: IModelDataHandler
    _afstand_var_data_handler: IModelDataHandler
    _afstand_berekenen: AfstandBerekenen
    _regel_data_handler: IModelDataHandler
    _regels: list

    def __init__(self):
        self._var_data_handler = VariabelenDataHandler()
        self._ber_var_data_handler = BerekendeVarDataHandler()
        self._afstand_var_data_handler = AfstandVarDataHandler()
        self._regel_data_handler = RegelDataHandler()
        self._regels = self._regel_data_handler.get_all_from_db()
        self._afstand_berekenen = AfstandBerekenen()

    # rekening houdem met regels rondom gebeurtenissen!

    # def controleer_regels_voor_jaar(self, jaar:int):

    def controleer_alle_regels_voor_jaar(self, jaar: int):
        for regel in self._regels:
            regel.results.append({regel.id, self._controleer_regel(regel, jaar)})
        return self._regels

    def _get_variabele_waarde_voor_jaar(self, varId: int, jaar):
        varKoppeling = self._var_data_handler.get_koppeling_from_id(varId)
        if varKoppeling.typeId == 1:
            return self._ber_var_data_handler.get_item_from_id(varId)
        elif varKoppeling.typeId == 2:
            return self._afstand_berekenen.get_laagste_afstand_van_var_uit_resultaat_voor_jaar(varId, jaar)
        elif varKoppeling.typeId == 1:
            return self._var_data_handler.get_item_from_id(varId)

    def _controleer_regel(self, regel, jaar: int):
        waarde1 = self._get_variabele_waarde_voor_jaar(regel.varId, jaar)
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
        elif regel.vergelijkingOperator == ">=" or regel.vergelijkingOperator == "=>":
            if waarde1 >= waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "<=" or regel.vergelijkingOperator == "=<" :
            if waarde1 <= waarde2:
                return True
            else:
                return False
        elif regel.vergelijkingOperator == "!=" or regel.vergelijkingOperator == "=!":
            if waarde1 != waarde2:
                return True
            else:
                return False
        else:
            return False

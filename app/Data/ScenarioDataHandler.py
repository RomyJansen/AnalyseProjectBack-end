from app.Data.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.DataHandler import DataHandler
from app.Data.VariabelenDataHandler import VariabelenDataHandler
from app.Models.Scenario import Scenario


class ScenarioDataHandler:

    _data_handler: DataHandler
    _var_data_handler: VariabelenDataHandler
    _bv_data_handler: BerekendeVarDataHandler

    def __init__(self):
        self._data_handler = DataHandler()
        self._var_data_handler = VariabelenDataHandler()
        self._bv_data_handler = BerekendeVarDataHandler()


    def get_scenario_from_db(self):
        varList = self._var_data_handler.get_start_variabelen()
        bvlist = self._bv_data_handler.get_all_bv_from_db()
        scenario = Scenario()
        scenario.standaard_variabelen = varList
        scenario.berekende_variabelen = bvlist

        return scenario
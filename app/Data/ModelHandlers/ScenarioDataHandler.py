from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Data.ModelHandlers.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.DataHandler import DataHandler
from app.Data.ModelHandlers.GebeurtenisDataHandler import GebeurtenisDataHandler
from app.Data.ModelHandlers.ObjectDataHandler import ObjectDataHandler
from app.Data.ModelHandlers.RegelDataHandler import RegelDataHandler
from app.Data.ModelHandlers.VariabelenDataHandler import VariabelenDataHandler
from app.Models.Scenario import Scenario


class ScenarioDataHandler:
    _data_handler: DataHandler
    _var_data_handler: VariabelenDataHandler
    _bv_data_handler: BerekendeVarDataHandler
    _object_data_handler: ObjectDataHandler
    _gebeurtenis_data_handler: GebeurtenisDataHandler
    _regel_data_handler: RegelDataHandler
    _afstand_berekenen: AfstandBerekenen

    def __init__(self):
        self._data_handler = DataHandler()
        self._var_data_handler = VariabelenDataHandler()
        self._bv_data_handler = BerekendeVarDataHandler()
        self._object_data_handler = ObjectDataHandler()
        self._gebeurtenis_data_handler = GebeurtenisDataHandler()
        self._regel_data_handler = RegelDataHandler()
        self._afstand_berekenen = AfstandBerekenen()

    def get_scenario_from_db(self):
        scenario = Scenario()
        scenario.standaard_variabelen = self._var_data_handler.get_all_from_db()
        scenario.berekende_variabelen = self._bv_data_handler.get_all_from_db()
        scenario.objecten = self._object_data_handler.get_all_from_db()
        scenario.afstands_variabelen = self._afstand_berekenen.bereken_alle_afstanden()
        scenario.gebeurtenissen = self._gebeurtenis_data_handler.get_objects_from_db()
        scenario.object_gebeurtenissen = self._gebeurtenis_data_handler.get_object_gebeurtenissen()
        scenario.regels = self._regel_data_handler.get_all_from_db()

        return scenario

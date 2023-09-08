from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Business.AnalyseComponent.BerVarBerekenen import BerVarBerekenen
from app.Business.AnalyseComponent.Controle import Controle
from app.Data.ModelHandlers.ScenarioDataHandler import ScenarioDataHandler
from app.Models.Scenario import Scenario


class AnalyseCore:
    _afstand_berekenen: AfstandBerekenen
    _ber_var_berekenen: BerVarBerekenen
    _scenario_data_handler: ScenarioDataHandler
    _controle: Controle

    def __init__(self):
        self._afstand_berekenen = AfstandBerekenen()
        self._ber_var_berekenen = BerVarBerekenen()
        self._scenario_data_handler = ScenarioDataHandler()
        self._controle = Controle()

    def analyse_uitvoeren(self, jaar):
        scenario_resultaten: Scenario = self._scenario_data_handler.get_scenario_from_db()
        scenario_resultaten.afstands_variabelen = self._afstand_berekenen.bereken_alle_afstanden()
        scenario_resultaten.berekende_variabelen = self._ber_var_berekenen.bereken_alle_berekende_var()
        scenario_resultaten.regels = self._controle.controleer_alle_regels_voor_jaar(jaar)
        return scenario_resultaten

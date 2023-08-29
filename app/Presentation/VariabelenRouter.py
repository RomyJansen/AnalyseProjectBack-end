from app.Business.AnalyseComponent.AfstandBerekenen import AfstandBerekenen
from app.Business.AnalyseComponent.BerVarBerekenen import BerVarBerekenen
from app.Business.AnalyseComponent.Controle import Controle
from app.Data.ModelHandlers.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.ModelHandlers.ScenarioDataHandler import ScenarioDataHandler

from fastapi import APIRouter

from app.Business.WijzigingsComponent.GebeurtenisController import GebeurtenisController

variabelen_router: APIRouter = APIRouter( prefix="/variabelen")
bv_data_handler: BerekendeVarDataHandler = BerekendeVarDataHandler()
bv_berekenen: BerVarBerekenen = BerVarBerekenen()
scenario_data_handler: ScenarioDataHandler = ScenarioDataHandler()
controle: Controle = Controle()
afstandBerekenen = AfstandBerekenen()
gebeurtenis_controller = GebeurtenisController()

@variabelen_router.get('/bv/{id}')
def get_berekende_variabele_from_id(id: int):
    return bv_data_handler.get_item_from_id(id)

@variabelen_router.get("/bv/berekening/{id}")
def get_berekende_waarde_van_variabele(id: int):
    return bv_berekenen.bereken_berekende_var(id)

@variabelen_router.get("/scenario")
def get_scenario():
    return scenario_data_handler.get_scenario_from_db()

@variabelen_router.get("/results")
def get_regel_results():
    return controle.controleer_alle_regels()

@variabelen_router.get("/afstanden")
def get_alle_afstanden():
    return afstandBerekenen.berekenAlleAfstanden()


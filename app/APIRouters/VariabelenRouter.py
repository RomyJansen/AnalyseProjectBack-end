from typing import Union

from app.Analyse.berekenen import Berekenen
from app.Data.BerekendeVarDataHandler import BerekendeVarDataHandler
from app.Data.DatabaseConnector import DatabaseConnector
from app.Models.BerekendeVar import BerekendeVar

from fastapi import FastAPI, APIRouter, Request

variabelen_router: APIRouter = APIRouter()
bv_data_handler: BerekendeVarDataHandler = BerekendeVarDataHandler()
bv_berekenen: Berekenen = Berekenen()

@variabelen_router.get('/bv/{id}')
def get_berekende_variabele_from_id(id: int):
    return bv_data_handler.get_item_from_id(id)

@variabelen_router.get("/bv/berekening/{id}")
def get_berekende_waarde_van_variabele(id: int):
    return bv_berekenen.bereken_berekende_var(id)
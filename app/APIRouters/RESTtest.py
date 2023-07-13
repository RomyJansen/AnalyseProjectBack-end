from typing import Union
from app.Data.util.DatabaseConnector import DatabaseConnector
from app.Models.BerekendeVar import BerekendeVar

from fastapi import APIRouter, Request

router: APIRouter = APIRouter()
dbc = DatabaseConnector()


@router.get("/hello")
def read_root():
    return {"Hello": "World"}


@router.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@router.post("/test/post")
def send_string_back(item: str):
    return {"Jij typte zojuist: " + item}


@router.post("/db")
async def get_items_from_database(request: Request):
    return dbc.connect( "select * from AlleVariabelen")


@router.post("/db/update")
async def updateBerekendeVar(newVar: BerekendeVar):
    newVar.printValues()
    return "all good!"

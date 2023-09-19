import mysql.connector
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.Data.ModelHandlers.GebeurtenisDataHandler import GebeurtenisDataHandler
from app.Models.Gebeurtenis import Gebeurtenis, ObjectGebeurtenis
from app.Business.WijzigingsComponent.GebeurtenisController import GebeurtenisController

gebeurtenissen_router: APIRouter = APIRouter(
    prefix="/gebeurtenis"
)
gebeurtenis_controller = GebeurtenisController()
gebeurtenis_data_handler = GebeurtenisDataHandler()


@gebeurtenissen_router.get("/get_gebeurtenissen")
def get_all_gebeurtenissen():
    return gebeurtenis_data_handler.get_objects_from_db()


@gebeurtenissen_router.get("/get_object_gebeurtenissen")
def get_all_object_gebeurtenissen():
    return gebeurtenis_data_handler.get_object_gebeurtenissen()


@gebeurtenissen_router.post("/toevoegen", status_code=201)
def post_gebeurtenis(gebeurtenis: Gebeurtenis):
    try:
        results = gebeurtenis_controller.add_gebeurtenis(gebeurtenis)
        return results
    except mysql.connector.Error as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="De gebeurtenis die je probeert toe te voegen bevat niet geoorloofde waardes.",
        )


@gebeurtenissen_router.post("/object/toevoegen", status_code=201)
def post_gebeurtenis(gebeurtenis: ObjectGebeurtenis):
    try:
        results = gebeurtenis_controller.add_Object_gebeurtenis(gebeurtenis)
        return results
    except mysql.connector.Error as e:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail="De gebeurtenis die je probeert toe te voegen bevat niet geoorloofde waardes.",
        )

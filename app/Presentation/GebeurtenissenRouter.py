import mysql.connector
from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from app.Models.Gebeurtenis import Gebeurtenis
from app.Business.WijzigingsComponent.GebeurtenisController import GebeurtenisController

gebeurtenissen_router: APIRouter = APIRouter(
    prefix="/gebeurtenis"
)
gebeurtenis_controller = GebeurtenisController()


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

from fastapi import APIRouter

from app.Models.Gebeurtenis import Gebeurtenis
from app.Business.WijzigingsComponent.GebeurtenisController import GebeurtenisController

gebeurtenissen_router: APIRouter = APIRouter(
    prefix="/gebeurtenis"
)
gebeurtenis_controller = GebeurtenisController()


@gebeurtenissen_router.post("/toevoegen")
def post_gebeurtenis(gebeurtenis: Gebeurtenis):
    return gebeurtenis_controller.add_gebeurtenis(gebeurtenis)

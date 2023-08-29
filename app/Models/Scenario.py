from typing import List

from pydantic import BaseModel

from app.Models.AfstandVar import AfstandVar
from app.Models.BerekendeVar import BerekendeVar
from app.Models.Variabele import Variabele


class Scenario(BaseModel):
    id: int = 1
    naam: str = "WijzigingsComponent"
    standaard_variabelen: List[Variabele] = []
    berekende_variabelen: List[BerekendeVar] = []
    afstands_variabelen: List[AfstandVar] = []
    gebeurtenissen: List[str] = []
    regels: List[str] = []
    objecten: List[str] = []
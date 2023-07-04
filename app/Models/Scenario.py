from pydantic import BaseModel


class Scenario(BaseModel):
    id: int = 1
    naam: str = "Scenario"
    standaard_variabelen: []
    berekende_variabelen: []
    gebeurtenissen: []
    regels: []
    objecten: []
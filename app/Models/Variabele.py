from pydantic import BaseModel


class Variabele(BaseModel):
    id: int
    naam: str
    waarde: int
    jaar: int


class VariabeleKoppeling(BaseModel):
    id: int
    typeId: int
    varId: int
    objectLink: int

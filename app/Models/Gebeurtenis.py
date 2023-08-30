from pydantic import BaseModel


class Gebeurtenis(BaseModel):
    id: int = 0
    naam: str = "naam"
    jaar: int = 0
    waarde: int = 0


class ObjectGebeurtenis(BaseModel):
    id: int = 0
    naam: str = "naam"
    jaar: int = 0
    locatieX: int = 0
    locatieY: int = 0

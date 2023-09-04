from pydantic import BaseModel


class Object(BaseModel):
    id: int = 0
    naam: str = "naam"
    objectType: int = 0
    locatieX: int = 0
    locatieY: int = 0
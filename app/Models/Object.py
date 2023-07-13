from pydantic import BaseModel


class Object(BaseModel):
    id: int = 0
    naam: str = "naam"
    objectType: str = "default"
    locatieX: int = 0
    locatieY: int = 0
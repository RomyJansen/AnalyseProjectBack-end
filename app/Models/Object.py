from pydantic import BaseModel


class Object(BaseModel):
    id: int = 0
    naam: str = "naam"
    objectType: int = 0
    locatieX: int = 0
    locatieY: int = 0
    grootteX: int = 0
    grootteY: int = 0
    jaar: int = 0
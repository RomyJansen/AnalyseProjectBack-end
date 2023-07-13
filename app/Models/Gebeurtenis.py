from pydantic import BaseModel


class Gebeurtenis(BaseModel):
    id: int = 0
    naam: str = "naam"
    varId: int = 0
    jaar: int = 0
    waarde: int = 0

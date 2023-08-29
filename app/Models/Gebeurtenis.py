from pydantic import BaseModel


class Gebeurtenis(BaseModel):
    id: int = 0
    naam: str = "naam"
    jaar: int = 0
    waarde: int = 0

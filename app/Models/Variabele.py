from pydantic import BaseModel


class Variabele(BaseModel):
    id: int
    naam: str
    waarde: int
    jaar: int

    # def __init__(self, id: int, naam: str, waarde: int):
    #     super().__init__()
    #     self.id = id
    #     self.naam = naam
    #     self.waarde = waarde

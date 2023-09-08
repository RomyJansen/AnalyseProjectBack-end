from pydantic import BaseModel

from app.Models.Variabele import Variabele


class BerekendeVar(Variabele):
    var1Id: int
    var2Id: int
    object1Id: int
    object2Id: int
    objectBerekening: bool
    operator: str
    results: list

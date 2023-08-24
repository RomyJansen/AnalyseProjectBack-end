from app.Models.Variabele import Variabele


class AfstandVar(Variabele):
    objectLink: int
    doelObjectType: int
    results: list


class ObjectType:
    id: int
    naam: str

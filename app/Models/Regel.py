from pydantic import BaseModel


class Regel(BaseModel):
    id: int = 0
    naam: str = "naam"
    waarde: int = 0
    vergelijkingOperator: str = "=="
    varId: int = 0
    results: list = []

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

    # def printValues(self):
    #     printString = "id: " + str(id)
    #     printString += "\nname: " + naam,
    #     printString += "\nwaarde: " + str(waarde)
    #     printString += "\nobjectBerekening: " + str(self.objectBerekening)
    #     if self.objectBerekening:
    #         printString += "\nobject1Id: " + str(self.object1Id)
    #         printString += "\nobject2Id: " + str(self.object2Id)
    #     else:
    #         printString += "\nvar1Id: " + str(self.var1Id)
    #         printString += "\nvar2Id: " + str(self.var2Id)

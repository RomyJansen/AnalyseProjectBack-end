from App.Models.Variabele import Variabele


class BerekendeVar(Variabele):
    var1Id: int
    var2Id: int
    object1Id: int
    object2Id: int
    objectBerekening: bool

    def __init__(self, id: int, naam: str, var1Id: int, var2Id: int, objectberekening: bool):
        super().__init__(id, naam, 0)
        self.objectBerekening = objectberekening
        if objectberekening:
            self.object1Id = var1Id
            self.object2Id = var2Id
        else:
            self.var1Id = var1Id
            self.var2Id = var2Id

    def printValues(self):
        printString = "id: " + str(super().id)
        printString += "\nname: " + super().name
        printString += "\nwaarde: " + str(super().waarde)
        printString += "\nobjectBerekening: " + str(self.objectBerekening)
        if self.objectBerekening:
            printString += "\nobject1Id: " + str(self.object1Id)
            printString += "\nobject2Id: " + str(self.object2Id)
        else:
            printString += "\nvar1Id: " + str(self.var1Id)
            printString += "\nvar2Id: " + str(self.var2Id)

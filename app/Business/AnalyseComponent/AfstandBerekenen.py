import math

from app.Business.IModelDataHandler import IModelDataHandler
from app.Data.ModelHandlers.AfstandVarDataHandler import AfstandVarDataHandler
from app.Data.ModelHandlers.ObjectDataHandler import ObjectDataHandler
from app.Models.AfstandVar import AfstandVar
from app.Models.Object import Object
from app.Models.Variabele import Variabele


class AfstandBerekenen:
    afstandVarDataHandler: IModelDataHandler = AfstandVarDataHandler()
    objectDataHandler: IModelDataHandler = ObjectDataHandler()

    def bereken_alle_afstanden(self):
        varResults: list = self.afstandVarDataHandler.get_all_from_db()
        objects: list = self.objectDataHandler.get_all_from_db()
        try:
            for item in varResults:
                item.results = self._bereken_afstand_voor_item(item, objects)
            return varResults
        except TypeError as e:
            raise (e, "Er zijn geen afstand variabelen in de database!")
        # Deze errorHandling verplaatsen naar data layer!

    def bereken_alle_afstanden_voor_jaar(self, jaar):
        varResults: list = self.afstandVarDataHandler.get_all_items_from_year(jaar)
        objects: list = self.objectDataHandler.get_all_items_from_year(jaar)
        try:
            for item in varResults:
                item.results = self._bereken_afstand_voor_item(item, objects)
            return varResults
        except TypeError as e:
            raise (e, "Er zijn geen afstand variabelen in de database!")
        # Deze errorHandling verplaatsen naar data layer!

    def _bereken_afstand_voor_item(self, item: AfstandVar, objects):
        results: list = []
        object: Object = self._find_specific_object(objects, item.objectLink)
        possibleObjects: list = []
        for o in objects:
            if o.objectType == item.doelObjectType:
                possibleObjects.append(o)

        for po in possibleObjects:
            results.append(Variabele(id=po.id, naam=po.naam,
                                     waarde=self._bereken_afstand(object.locatieX, object.locatieY, po.locatieX,
                                                                  po.locatieY), jaar=po.jaar))

        return results

    def get_laagste_afstand_van_var_uit_resultaat_voor_jaar(self, id: int, jaar: int):
        results = self.bereken_alle_afstanden_voor_jaar(jaar)
        for var in results:
            if var.id == id:
                return self._find_lowest_distance(var)

    def _find_lowest_distance(self, afstand_var: AfstandVar):
        lowest: int = 0
        for var in afstand_var.results:
            if lowest == 0:
                lowest = var.waarde
            elif var.waarde < lowest:
                lowest = var.waarde
        return lowest

    def _find_specific_object(self, objects: list, id: int):
        try:
            for o in objects:
                if o.id == id:
                    return o
        except TypeError as e:
            raise(TypeError, "list of objects is empty!")

    def _bereken_afstand(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


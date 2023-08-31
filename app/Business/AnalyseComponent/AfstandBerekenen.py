import math

from app.Data.ModelHandlers.AfstandVarDataHandler import AfstandVarDataHandler
from app.Data.ModelHandlers.ObjectDataHandler import ObjectDataHandler
from app.Models.AfstandVar import AfstandVar
from app.Models.Object import Object
from app.Models.Variabele import Variabele


class AfstandBerekenen:

    afstandVarDataHandler = AfstandVarDataHandler()
    objectDataHandler = ObjectDataHandler()

    def berekenAlleAfstanden(self):
        varResults: list = self.afstandVarDataHandler.get_all_bv_from_db()
        objects: list = self.objectDataHandler.get_objects_from_db()
        for item in varResults:
            item.results = self.bereken_afstand_voor_item(item, objects)
        return varResults

    def bereken_alle_afstanden_voor_jaar(self, jaar):
        varResults: list = self.afstandVarDataHandler.get_all_items_from_year(jaar)
        objects: list = self.objectDataHandler.get_all_items_from_year(jaar)
        for item in varResults:
            item.results = self.bereken_afstand_voor_item(item, objects)
        return varResults

    def bereken_afstand_voor_item(self, item: AfstandVar, objects):
        results: list = []
        object: Object = self._find_specific_object(objects, item.objectLink)
        possibleObjects: list = []
        for o in objects:
            if o.objectType == item.doelObjectType:
                possibleObjects.append(o)

        for po in possibleObjects:
            results.append(Variabele(id=po.id, naam=po.naam, waarde=self._bereken_afstand(object.locatieX, object.locatieY, po.locatieX, po.locatieY), jaar=0))

        return results

    def _find_specific_object(self, objects: list, id: int):
        for o in objects:
            if o.id == id:
                return o

    # def _find_specific_objecttype(self, objects: list[ObjectType], id: int):
    #     for o in objects:
    #         if o.id == id:
    #             return o


    def _bereken_afstand(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

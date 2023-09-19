from app.Business.AnalyseComponent.AnalyseCore import AnalyseCore
from app.Business.IModelDataHandler import IModelDataHandler
from app.Data.ModelHandlers.GebeurtenisDataHandler import GebeurtenisDataHandler
from app.Models.Gebeurtenis import Gebeurtenis, ObjectGebeurtenis


class GebeurtenisController():
    gebeurtenis_data_handler: IModelDataHandler
    analyse_core: AnalyseCore

    def __init__(self):
        self.gebeurtenis_data_handler = GebeurtenisDataHandler()
        self.analyse_core = AnalyseCore()

    def add_gebeurtenis(self, gebeurtenis: Gebeurtenis):
        self.gebeurtenis_data_handler.add_gebeurtenis_to_db(gebeurtenis)
        resultaten = self.analyse_core.analyse_uitvoeren(gebeurtenis.jaar)

        return resultaten

    def add_Object_gebeurtenis(self, gebeurtenis: ObjectGebeurtenis):
        self.gebeurtenis_data_handler.add_object_gebeurtenis_to_db(gebeurtenis)
        resultaten = self.analyse_core.analyse_uitvoeren(gebeurtenis.jaar)

        return resultaten

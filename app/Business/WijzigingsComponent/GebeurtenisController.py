from app.Business.AnalyseComponent.AnalyseCore import AnalyseCore
from app.Data.ModelHandlers.GebeurtenisDataHandler import GebeurtenisDataHandler
from app.Models.Gebeurtenis import Gebeurtenis


class GebeurtenisController():
    gebeurtenis_data_handler: GebeurtenisDataHandler
    analyse_core: AnalyseCore

    def __init__(self):
        self.gebeurtenis_data_handler = GebeurtenisDataHandler()
        self.analyse_core = AnalyseCore()

    def add_gebeurtenis(self, gebeurtenis: Gebeurtenis):
        self.gebeurtenis_data_handler.add_gebeurtenis_to_db(gebeurtenis)
        resultaten = self.analyse_core.analyse_uitvoeren()

        return resultaten

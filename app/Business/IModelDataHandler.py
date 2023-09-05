from abc import ABC, abstractmethod


class IModelDataHandler(ABC):

    @abstractmethod
    def get_item_from_id(self, id: int):
        pass

    @abstractmethod
    def get_all_from_db(self):
        pass

    @abstractmethod
    def _put_result_into_object(self, result: []):
        pass

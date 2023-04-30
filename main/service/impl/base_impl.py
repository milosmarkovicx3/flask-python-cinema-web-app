from abc import ABC, abstractmethod

from entities.core.result import Result
from service.utility.logger import log
from service.utility.utility import json


class BaseImpl(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T()

    def get_by_id(self, id):
        try:
            result = Result(item=self.T.find_by(id))
            if result.get_item() is False:
                result.set_status_with_description(Result.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(e)
            result = Result()
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)

    def get_all(self):
        try:
            result = Result(item=self.T.get_all())
            if result.get_item() is False:
                result.set_status_with_description(Result.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(e)
            result = Result()
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)

    def delete_by_id(self, id):
        try:
            result = Result(item=self.T.delete_by_id(id))
            if result.get_item() is False:
                result.set_status_with_description(Result.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(e)
            result = Result()
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
            return json(result)
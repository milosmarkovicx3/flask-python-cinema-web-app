import traceback
from abc import ABC, abstractmethod
from entities.core.result import Result
from entities.core.status import Status
from service.utility.logger import log
from service.utility.utils import json


class BaseImpl(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T()

    def find_by(self, value, column):
        try:
            result = Result(item=self.T.find_by(value, column))
            if result.get_item() is False:
                result.set_status(Status.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)

    def get_all(self):
        try:
            result = Result(item=self.T.get_all())
            if result.get_item() is False:
                result.set_status(Status.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)

    def delete_by_id(self, id):
        try:
            result = Result(item=self.T.delete_by_id(id))
            if result.get_item() is False:
                result.set_status(Status.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
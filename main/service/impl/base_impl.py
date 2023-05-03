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

    def find(self, value, column):
        return __result_handler__(item=self.T.find(value, column))

    def find_all(self, **kwargs):
        return __result_handler__(item=self.T.find_all(**kwargs))

    def delete(self, value, column):
        return __result_handler__(item=self.T.delete(value, column))


def __result_handler__(item):
    try:
        result = Result(item=item)
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


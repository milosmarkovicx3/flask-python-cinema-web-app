import traceback
from abc import ABC, abstractmethod
from main.entities.core.result import Result
from main.entities.core.status import Status
from main.service.utility.logger import log

class BaseImpl(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T()

    def find(self, value, column):
        return _result_handler(item=self.T.find(value, column))

    def find_all(self, kwargs):
        return _result_handler(item=self.T.find_all(**kwargs))

    def delete(self, value, column):
        return _result_handler(item=self.T.delete(value, column))


def _result_handler(item):
    try:
        result = Result(item=item)
        if item is False:
            result.set_status(Status.NOT_FOUND)
        elif item is None:
            result.set_status(Status.INTERNAL_SERVER_ERROR)
        return result.response()
    except Exception as e:
        log.error(f"{e}\n{traceback.format_exc()}")
        result = Result(status=Status.INTERNAL_SERVER_ERROR)
        return result.response()


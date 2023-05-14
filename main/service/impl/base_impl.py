from abc import ABC, abstractmethod
from main.entities.core.result import result_handler


class BaseImpl(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T()

    def find(self, value, column):
        return result_handler(item=self.T.find(value, column))

    def find_all(self, kwargs):
        return result_handler(item=self.T.find_all(**kwargs))

    def delete(self, data):
        return result_handler(item=self.T.delete(data))


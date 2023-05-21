import inspect
from abc import ABC
from main.entities.core.result import result_handler

class BaseImpl(ABC):
    def __init__(self, T):
        self.T = T()

    def find(self, **kwargs):
        valid_kwargs = {k: v for k, v in kwargs.items() if v and k in inspect.signature(self.T.find).parameters}
        return result_handler(item=self.T.find(**valid_kwargs))

    def find_all(self, **kwargs):
        valid_kwargs = {k: v for k, v in kwargs.items() if v and k in inspect.signature(self.T.find_all).parameters}
        return result_handler(item=self.T.find_all(**valid_kwargs))


    def delete(self, **kwargs):
        valid_kwargs = {k: v for k, v in kwargs.items() if v and k in inspect.signature(self.T.delete).parameters}
        return result_handler(item=self.T.delete(**valid_kwargs))


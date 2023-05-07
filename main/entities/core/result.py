from json import dumps
from flask import Response
from main.entities.core.status import Status



class Result:
    def __init__(self, item=None, status=Status.OK, description=None):
        self._item = item
        self._status = status.value
        if description is not None:
            self._description = description
        else:
            self._description = status.name

    def get_item(self):
        return self._item

    def get_status(self):
        return self._status

    def get_description(self):
        return self._description

    def set_item(self, item):
        self._item = item

    def set_status(self, status):
        self._status = status.value
        self._description = status.name

    def set_description(self, description):
        self._description = description

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return {
            "status": self._status,
            "description": self._description,
            "item": self._item.__repr__()
        }

    def response(self):
        json_data = dumps(self.__repr__(), sort_keys=False, indent=4, ensure_ascii=False)
        return Response(json_data, content_type='application/json')
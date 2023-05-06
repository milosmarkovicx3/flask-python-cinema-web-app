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
        return str(self.__repr__())

    def __repr__(self):
        return {
            "status": self._status,
            "description": self._description,
            "item": self.__repr_helper_method__()
        }

    def __repr_helper_method__(self):
        if not isinstance(self._item, list):
            return self._item.__repr__()
        _list = []
        for item in self._item:
            if isinstance(item, list):
                _sub_list = []
                for sub_item in item:
                    _sub_list.append(sub_item.__repr__())
                _list.append(_sub_list)
            else:
                _list.append(item.__repr__())
        return _list

class Result:
    OK = "200"
    BAD_REQUEST = "400"
    UNAUTHORIZED = "401"
    FORBIDDEN = "403"
    NOT_FOUND = "404"
    INTERNAL_SERVER_ERROR = "500"

    def __init__(self, item=None, status=OK, description="OK"):
        self._item = item
        self._status = status
        self._description = description

    def get_item(self):
        return self._item

    def get_status(self):
        return self._status

    def get_description(self):
        return self._description

    def set_item(self, item):
        self._item = item

    def set_status(self, status):
        self._status = status

    def set_status_with_description(self, status):
        self._status = status
        if status == "200":
            self._description = "OK"
        elif status == "400":
            self._description = "BAD_REQUEST"
        elif status == "401":
            self._description = "UNAUTHORIZED"
        elif status == "403":
            self._description = "FORBIDDEN"
        elif status == "404":
            self._description = "NOT_FOUND"
        elif status == "500":
            self._description = "INTERNAL_SERVER_ERROR"

    def set_description(self, description):
        self._description = description

    def _repr_helper(self):
        if not isinstance(self._item, list):
            return self._item.__repr__()
        lst = []
        for item in self._item:
            if isinstance(item, list):
                sub_lst = []
                for sub_item in item:
                    sub_lst.append(sub_item.__repr__())
                lst.append(sub_lst)
            else:
                lst.append(item.__repr__())
        return lst

    def __repr__(self):
        return {
            "status": self._status,
            "description": self._description,
            "item": self._repr_helper()
        }


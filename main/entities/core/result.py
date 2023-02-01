class Result:

    OK = "200"
    BAD_REQUEST = "400"
    UNAUTHORIZED = "401"
    FORBIDDEN = "403"
    NOT_FOUND = "404"
    INTERNAL_SERVER_ERROR = "500"

    def __init__(self, item = None, status = OK, description = "OK"):
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
    def set_description(self, description):
        self._description = description

    def __repr__(self):
        return {
            "status": self._item,
            "description": self._description,
            "item": self._item
        }


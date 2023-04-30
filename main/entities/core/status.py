import enum

class Status(enum.Enum):
    OK = "200"
    NOT_MODIFIED = "304"            # resurs nije modifovan od poslednje posete, koristi kešerin
    BAD_REQUEST = "400"
    UNAUTHORIZED = "401"
    FORBIDDEN = "403"
    NOT_FOUND = "404"
    CONFLICT = "409"
    INTERNAL_SERVER_ERROR = "500"

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {self.name : self.value}


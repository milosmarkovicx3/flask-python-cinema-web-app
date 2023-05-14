import traceback
from json import dumps
from flask import Response
from main.entities.core.status import Status
from main.service.utility.logger import log
from main.service.utility.utils import repr_helper_method


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

    def response(self):
        """
        Zamena za flask.jsonify, jer je tamo default-no ponašanje da se
        sortiraju vrednosti u json formatu.
        :param sort_keys: Potvrđujemo da nećemo sortiranje.
        :param indent: Unosimo uvučeni deo teksta za vrednosti, umesto
        samo jednog prostog paragrafa za ceo json izlaz.
        :param ensure_ascii: Parametar koji omogućava prikaz UTF-8 slova.
        :return: Flask response, čiji je tip vraćenih podataka json.
        """
        json_data = dumps(self.__repr__(), sort_keys=False, indent=4, ensure_ascii=False)
        return Response(json_data, content_type='application/json')

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "status": self._status,
            "description": self._description,
            "item": repr_helper_method(self._item)
        }

def result_handler(item):
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

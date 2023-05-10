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
            "item": self._repr_helper_method()
        }

    def _repr_helper_method(self):
        """
        Kada se self.item lista, a ne jedan objekat.
        :param self._item: Bilo koja potencijalna lista objekata.
        :return: Listu rečnika koji predstavljaju konvertovane objekte.
        """
        if not isinstance(self._item, list):
            return self._item.__repr__()
        _list = []
        for item in self._item:
            if isinstance(item, list):
                _sub_list = self._repr_helper_method(item)
                _list.append(_sub_list)
            else:
                _list.append(item.__repr__())
        return _list


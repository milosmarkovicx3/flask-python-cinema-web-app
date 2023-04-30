from abc import ABC, abstractmethod

from entities.core.base import db
from service.utility.logger import log
from service.utility.utility import json


class BaseFacade(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T

    def find_by(self, value, column="id"):
        try:
            log.info(f'id: {id}')
            response = db.session.query(self.T).filter(self.T.id == id).first()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(e)
            return None

    def get_all(self):
        try:
            response = db.session.query(self.T).all()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(e)
            return None

    def delete_by_id(self, id):
        try:
            log.info(f'id: {id}')
            response = db.session.query(self.T).filter(self.T.id == id).first()
            if response is None:
                return False
            db.session.delete(response)
            db.session.commit()
            return response
        except Exception as e:
            log.error(e)
            db.rollback()
            return None
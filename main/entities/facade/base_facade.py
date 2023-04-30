import traceback
from abc import ABC, abstractmethod
from entities.core.base import db
from service.utility.logger import log

class BaseFacade(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T

    def find_by(self, value, column):
        try:
            log.info(f'value: {value}, column: {column}')
            response = db.session.query(self.T).filter_by(**{column: value}).first()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

    def get_all(self):
        try:
            response = db.session.query(self.T).all()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
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
            log.error(f"{e}\n{traceback.format_exc()}")
            db.rollback()
            return None
import traceback
from abc import ABC, abstractmethod
from entities.core.base import db
from service.utility.logger import log

class BaseFacade(ABC):
    @abstractmethod
    def __init__(self, T):
        self.T = T

    def find(self, value, column):
        try:
            log.info(f'value: {value}, column: {column}')
            response = db.session.query(self.T).filter_by(**{column: value}).first()
            return False if response is None else response
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

    def find_all(self, **kwargs):
        try:
            query = self.T.query
            for column, value in kwargs.items():
                if value is not None:
                    query = query.filter_by(**{column: value})
            response = query.all()
            return False if response is None else response
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

    def create(self, entity):
        try:
            log.info(f'user: {entity}')
            if not isinstance(entity, self.T):
                return False
            db.session.add(entity)
            db.session.commit()
            return entity
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            db.rollback()
            return None

    def delete(self, value, column):
        try:
            log.info(f'value: {value}, column: {column}')
            response = db.session.query(self.T).filter_by(**{column: value}).first()
            if response is None:
                return False
            db.session.delete(response)
            db.session.commit()
            return True
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            db.rollback()
            return None
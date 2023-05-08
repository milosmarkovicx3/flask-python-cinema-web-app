import traceback
from abc import ABC, abstractmethod
from main.entities.core.base import db
from main.service.utility.logger import log

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

    def find_all(self, column=None, value1=None, value2=None, method=None, max=None):
        try:
            query = self.T.query

            if column is None:
                response = query.all()
                return False if response is None else response

            column = getattr(self.T, column)

            if value1 is not None:
                if method is not None:
                    if method == 'like':
                        query = query.filter(column.like(f"%{value1}%"))
                    elif method == 'less':
                        query = query.filter(column <= value1)
                    elif method == 'higher':
                        query = query.filter(column >= value2)
                elif value2 is not None:
                    query = query.filter(column.between(value1, value2))

            if max is not None:
                query = query.limit(max)

            response = query.all()
            return False if response is None else response
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

    def create(self, entity):
        try:
            log.info(f'create: {entity}')
            if not isinstance(entity, self.T):
                return False
            db.session.add(entity)
            db.session.commit()
            return entity
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            db.session.rollback()
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
            db.session.rollback()
            return None
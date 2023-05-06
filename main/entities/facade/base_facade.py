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

    def find_all(self, kwargs):
        try:
            query = self.T.query

            if 'column' not in kwargs:
                return False

            column = getattr(self.T, kwargs['column'])

            if 'value1' in kwargs:
                if 'method' in kwargs:
                    if kwargs['method'] == 'like':
                        query = query.filter(column.like(f"%{kwargs['value1']}%"))
                    elif kwargs['method'] == 'less':
                        query = query.filter(column <= kwargs['value1'])
                    elif kwargs['method'] == 'higher':
                        query = query.filter(column >= kwargs['value1'])
                elif 'value2' in kwargs:
                    query = query.filter(column.between(kwargs['value1'], kwargs['value2']))
                if 'max' in kwargs:
                    query = query.limit(kwargs['max'])

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
from abc import ABC
from main.entities.core.base import db
from main.service.utility.logger import log

class BaseFacade(ABC):
    def __init__(self, T):
        self.T = T

    def find(self, value, column='id'):
        try:
            response = db.session.query(self.T).filter_by(**{column: value}).first()
            return response or False
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return None

    def find_all(self, column=None, value=None, value_to=None, method=None, max=None):
        try:
            query = self.T.query

            if column is not None:
                column = getattr(self.T, column)

                if value is not None:
                    if value_to is not None:
                        query = query.filter(column.between(value, value_to))
                    elif method == 'less':
                        query = query.filter(column <= value)
                    elif method == 'higher':
                        query = query.filter(column >= value_to)
                    else:
                        query = query.filter(column.like(f"%{value}%"))

            if max is not None:
                query = query.limit(max)

            response = query.all()
            return response or False
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return None

    def create(self, entity):
        try:
            if not isinstance(entity, self.T):
                return False
            db.session.add(entity)
            db.session.commit()
            return entity
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            db.session.rollback()
            return None

    def delete(self, value, column='id'):
        try:
            response = db.session.query(self.T).filter_by(**{column: value}).first()
            if response is None:
                return False
            db.session.delete(response)
            db.session.commit()
            return True
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            db.session.rollback()
            return None

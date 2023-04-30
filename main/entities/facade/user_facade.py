from entities.facade.base_facade import BaseFacade
from entities.models.user import User
from service.utility.logger import log
from entities.core.base import db
from service.utility.utility import json


class UserFacade(BaseFacade):
    def __init__(self):
        super().__init__(User)

    def create(self, user):
        try:
            log.info(user)
            if not isinstance(user, User):
                return False
            db.session.add(user)
            db.session.commit()
            return user
        except Exception as e:
            log.error(e)
            db.rollback()
            return None

    def find_by(self, column, value):
        return db.session.query(User).filter_by(**{column: value}).first()

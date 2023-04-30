import traceback
from datetime import datetime
from entities.core.result import Result
from entities.core.status import Status
from entities.facade.user_facade import UserFacade
from entities.models.user import User
from service.impl.base_impl import BaseImpl
from service.utility.logger import log
from service.utility.utility import json


class UserImpl(BaseImpl):
    def __init__(self):
        super().__init__(UserFacade)

    def create(self, data):
        log.info(data)
        try:
            result = Result()
            if self.T.find_by(data['register-username'], "username"):
                result.set_status(Status.CONFLICT)
                result.set_description("Korisnik sa tim korisničkim imenom već postoji!")
                return json(result)

            if self.T.find_by(data['register-email'], "email"):
                result.set_status(Status.CONFLICT)
                result.set_description("Korisnik sa tom email adresom već postoji!")
                return json(result)

            user = User(
                first_name=data['register-first-name'],
                last_name=data['register-last-name'],
                email=data['register-email'],
                username=data['register-username'],
                password=data['register-passwd'],
                date_joined=datetime.now(),
                last_login_at=datetime.now(),
                login_count=1
            )

            result.set_item(self.T.create(user))

            if result.get_item() is False:
                result.set_status(Status.BAD_REQUEST, True)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR, True)
            return json(result)
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR, True)
            return json(result)


import traceback

from entities.facade.base_facade import BaseFacade
from entities.models.user import User
from service.utility.logger import log
from entities.core.base import db
from service.utility.utils import json


class UserFacade(BaseFacade):
    def __init__(self):
        super().__init__(User)



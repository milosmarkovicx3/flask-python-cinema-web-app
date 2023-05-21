from main.entities.facade.base_facade import BaseFacade
from main.entities.models.user import User

class UserFacade(BaseFacade):
    def __init__(self):
        super().__init__(User)



from main.entities.facade.base_facade import BaseFacade
from main.entities.models.hall import Hall


class HallFacade(BaseFacade):
    def __init__(self):
        super().__init__(Hall)



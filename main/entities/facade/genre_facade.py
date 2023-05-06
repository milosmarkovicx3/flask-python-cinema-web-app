from main.entities.facade.base_facade import BaseFacade
from main.entities.models.genre import Genre

class GenreFacade(BaseFacade):
    def __init__(self):
        super().__init__(Genre)




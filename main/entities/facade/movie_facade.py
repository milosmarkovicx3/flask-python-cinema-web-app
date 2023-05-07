from main.entities.facade.base_facade import BaseFacade
from main.entities.models.movie import Movie


class MovieFacade(BaseFacade):
    def __init__(self):
        super().__init__(Movie)





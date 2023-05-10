from main.entities.facade.base_facade import BaseFacade
from main.entities.models.review import Review


class ReviewFacade(BaseFacade):
    def __init__(self):
        super().__init__(Review)



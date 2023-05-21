from main.entities.facade.base_facade import BaseFacade
from main.entities.models.projection import Projection

class ProjectionFacade(BaseFacade):
    def __init__(self):
        super().__init__(Projection)



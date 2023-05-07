from main.entities.facade.projection_facade import ProjectionFacade
from main.service.impl.base_impl import BaseImpl


class ProjectionImpl(BaseImpl):
    def __init__(self):
        super().__init__(ProjectionFacade)
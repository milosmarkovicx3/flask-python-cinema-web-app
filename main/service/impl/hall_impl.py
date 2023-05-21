from main.entities.facade.hall_facade import HallFacade
from main.service.impl.base_impl import BaseImpl

class HallImpl(BaseImpl):
    def __init__(self):
        super().__init__(HallFacade)
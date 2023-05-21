from main.entities.facade.base_facade import BaseFacade
from main.entities.models.seat import Seat

class SeatFacade(BaseFacade):
    def __init__(self):
        super().__init__(Seat)



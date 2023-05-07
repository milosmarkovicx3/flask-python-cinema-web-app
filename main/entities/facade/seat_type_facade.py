from main.entities.facade.base_facade import BaseFacade
from main.entities.models.seat_type import SeatType


class SeatTypeFacade(BaseFacade):
    def __init__(self):
        super().__init__(SeatType)



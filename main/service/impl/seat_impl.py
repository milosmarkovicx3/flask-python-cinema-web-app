from main.entities.facade.seat_facade import SeatFacade
from main.service.impl.base_impl import BaseImpl


class SeatImpl(BaseImpl):
    def __init__(self):
        super().__init__(SeatFacade)
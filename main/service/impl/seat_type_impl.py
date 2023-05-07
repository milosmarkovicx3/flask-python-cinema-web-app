from main.entities.facade.seat_type_facade import SeatTypeFacade
from main.service.impl.base_impl import BaseImpl


class SeatTypeImpl(BaseImpl):
    def __init__(self):
        super().__init__(SeatTypeFacade)
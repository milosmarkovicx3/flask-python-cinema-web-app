from main.entities.facade.reservation_facade import ReservationFacade
from main.service.impl.base_impl import BaseImpl


class ReservationImpl(BaseImpl):
    def __init__(self):
        super().__init__(ReservationFacade)
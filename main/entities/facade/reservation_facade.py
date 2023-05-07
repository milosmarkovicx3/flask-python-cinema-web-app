from main.entities.facade.base_facade import BaseFacade
from main.entities.models.reservation import Reservation


class ReservationFacade(BaseFacade):
    def __init__(self):
        super().__init__(Reservation)



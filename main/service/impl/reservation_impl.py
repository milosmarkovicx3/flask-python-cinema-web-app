import traceback

from flask_login import current_user
from main.entities.core.base import db
from main.entities.core.result import Result, result_handler
from main.entities.core.status import Status
from main.entities.facade.reservation_facade import ReservationFacade
from main.entities.models.reservation import Reservation
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log


class ReservationImpl(BaseImpl):
    def __init__(self):
        super().__init__(ReservationFacade)

    def create(self, data):
        try:
            projection_id = data['projection_id']
            seat_id = data['seat_id']

            if not current_user.is_authenticated:
                result = Result(
                    status=Status.UNAUTHORIZED,
                    description='Error: samo ulogovani korisnici mogu da kreiraju rezervacije.'
                )
                return result.response()

            user_id = current_user.get_id()

            reservation = Reservation.query \
                .filter(Reservation.projection_id == projection_id) \
                .filter(Reservation.seat_id == seat_id)\
                .first()

            if reservation:
                result = Result(
                    status=Status.BAD_REQUEST,
                    description=f'Error: rezervacija za dato sedište već postoji.\n{reservation.__repr__()}')
                return result.response()

            reservation = Reservation(projection_id=projection_id, seat_id=seat_id, user_id=user_id)
            db.session.add(reservation)
            db.session.commit()

            return result_handler(item=True)
        except Exception as e:
            db.session.rollback()
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()

from flask_login import current_user
from main.entities.core.base import db
from main.entities.core.result import Result, result_handler
from main.entities.core.status import Status
from main.entities.facade.projection_facade import ProjectionFacade
from main.entities.facade.reservation_facade import ReservationFacade
from main.entities.facade.seat_facade import SeatFacade
from main.entities.models.reservation import Reservation
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log
from main.service.utility.mail import send_mail_create_reservation
from main.service.utility.utils import repr_format_date, repr_format_time

pf = ProjectionFacade()
sf = SeatFacade()

class ReservationImpl(BaseImpl):
    def __init__(self):
        super().__init__(ReservationFacade)

    def create(self, form):
        reservation = ''
        try:
            projection_id = form.get('projection_id')
            seat_id = form.get('seat_id')

            if not current_user.is_authenticated:
                return Result(status=Status.UNAUTHORIZED).response()

            user_id = current_user.id

            reservation = Reservation.query \
                .filter(Reservation.projection_id == projection_id) \
                .filter(Reservation.seat_id == seat_id)\
                .first()

            if reservation or not pf.find(value=projection_id) or not sf.find(value=seat_id):
                return Result(status=Status.BAD_REQUEST).response()

            reservation = Reservation(
                projection_id=projection_id,
                seat_id=seat_id,
                user_id=user_id
            )
            db.session.add(reservation)
            db.session.commit()

            send_mail_create_reservation(
                msg_to=current_user.email,
                reservation_id=reservation.id,
                movie=reservation.projection.movie.title,
                date=repr_format_date(reservation.projection.date),
                time=repr_format_time(reservation.projection.time_from),
                seat=f'R{reservation.seat.row} #{reservation.seat.number}'
            )
            return Result().response()
        except Exception as e:
            if reservation and reservation.id:
                db.session.delete(reservation)
                db.session.commit()
            db.session.rollback()
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()

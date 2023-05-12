import traceback
from datetime import datetime

from main.entities.core.base import db
from main.entities.facade.base_facade import BaseFacade
from main.entities.models.projection import Projection
from main.entities.models.reservation import Reservation
from main.service.utility.logger import log


class ReservationFacade(BaseFacade):
    def __init__(self):
        super().__init__(Reservation)

    def find_all(self, column=None, value=None, value_to=None, method=None, max=None):
        try:
            reservations = super().find_all(column, value, value_to, method, max)
            if not reservations:
                return False

            old_reservations_for_deletion = []
            now = datetime.now()

            for reservation in reservations:
                p = Projection.query.filter_by(id=reservation.projection_id).first()
                if p is None or p.date < now.date() or (p.date == now.date() and p.time < now.time()):
                    old_reservations_for_deletion.append(reservation)

            for r in old_reservations_for_deletion:
                reservations.remove(r)
                db.session.delete(r)

            db.session.commit()

            return reservations
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

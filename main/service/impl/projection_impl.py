import traceback
from datetime import datetime, timedelta

from sqlalchemy import and_, between, not_

from main.entities.core.result import Result
from main.entities.core.status import Status
from main.entities.facade.projection_facade import ProjectionFacade
from main.entities.models.projection import Projection
from main.service.impl.base_impl import BaseImpl, _result_handler
from main.service.utility.logger import log


class ProjectionImpl(BaseImpl):
    def __init__(self):
        super().__init__(ProjectionFacade)

    def create(self, data):
        try:
            log.info(str(data))
            movie_id = data['projection-movie']
            hall_id = data['projection-hall']
            date_from = data['projection-from']
            date_to = data['projection-to']
            time = datetime.strptime(data['projection-time'], '%H:%M').time()

            start_time = (datetime.combine(datetime.min, time) - timedelta(minutes=165)).time()
            end_time = (datetime.combine(datetime.min, time) + timedelta(minutes=180)).time()

            query = Projection.query.filter(
                and_(
                    between(Projection.time, start_time, end_time),
                    Projection.date_from <= date_to
                )
            )
            projection = query.first()

            if projection:
                result = Result(
                    status=Status.BAD_REQUEST,
                    description=f'projekcija u datom terminu već postoji.\n{projection.__repr__()}')
                return result.response()

            projection = Projection(movie_id=movie_id, hall_id=hall_id, date_from=date_from, date_to=date_to, time=time)

            return _result_handler(item=self.T.create(projection))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


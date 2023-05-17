import traceback
from datetime import datetime, timedelta
import re

from main.entities.core.base import db
from main.entities.core.result import Result, result_handler
from main.entities.core.status import Status
from main.entities.facade.movie_facade import MovieFacade
from main.entities.facade.projection_facade import ProjectionFacade
from main.entities.models.projection import Projection
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log


class ProjectionImpl(BaseImpl):
    def __init__(self):
        super().__init__(ProjectionFacade)

    def create(self, data):
        try:
            movie_id = data['projection-movie']
            hall_id = data['projection-hall']
            date_from = datetime.strptime(data['projection-from'], '%Y-%m-%d').date()
            date_to = datetime.strptime(data['projection-to'], '%Y-%m-%d').date()
            time = datetime.strptime(data['projection-time'], '%H:%M').time()

            mf = MovieFacade()
            movie = mf.find(column='id', value=movie_id)

            hours = re.search(r'(\d+)h', movie.duration).group(1)
            minutes = re.search(r'(\d+)m', movie.duration).group(1)
            total_minutes = int(hours) * 60 + int(minutes)

            time_after = datetime.combine(datetime.today(), time) + timedelta(minutes=total_minutes)

            current_date = date_from
            while current_date <= date_to:
                projection = Projection.query\
                    .filter(Projection.hall_id == hall_id)\
                    .filter(Projection.date == current_date)\
                    .filter(Projection.time.between(time, time_after.time()))\
                    .first()

                if projection:
                    result = Result(
                        status=Status.BAD_REQUEST,
                        description=f'Error: projekcija u datom terminu već postoji.\n{projection.__str__()}')
                    return result.response()

                projection = Projection(hall_id=hall_id, movie_id=movie_id, date=current_date, time=time)
                db.session.add(projection)
                current_date += timedelta(days=1)

            db.session.commit()

            return result_handler(item=True)
        except Exception as e:
            db.session.rollback()
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


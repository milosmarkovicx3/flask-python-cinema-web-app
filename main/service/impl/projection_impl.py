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

mf = MovieFacade()

class ProjectionImpl(BaseImpl):
    def __init__(self):
        super().__init__(ProjectionFacade)

    def create(self, form):
        try:
            movie_id = form.get('projection-movie')
            hall_id = form.get('projection-hall')
            date_from = datetime.strptime(form.get('projection-from'), '%Y-%m-%d').date()
            date_to = datetime.strptime(form.get('projection-to'), '%Y-%m-%d').date()
            time_from = datetime.strptime(form.get('projection-time'), '%H:%M').time()

            movie = mf.find(value=movie_id)

            hours = re.search(r'(\d+)h', movie.duration).group(1)
            minutes = re.search(r'(\d+)m', movie.duration).group(1)
            total_minutes = int(hours) * 60 + int(minutes)

            time_to = datetime.combine(datetime.today(), time_from) + timedelta(minutes=total_minutes)

            current_date = date_from
            while current_date <= date_to:
                projection = Projection.query\
                    .filter(Projection.hall_id == hall_id)\
                    .filter(Projection.date == current_date)\
                    .filter(Projection.time_to >= time_from)\
                    .filter(Projection.time_from <= time_to)\
                    .first()

                if projection:
                    return Result(
                        status=Status.BAD_REQUEST,
                        description=f'Projekcija u izabranom terminu već postoji. {projection}'
                    ).response()

                projection = Projection(
                    hall_id=hall_id,
                    movie_id=movie_id,
                    date=current_date,
                    time_from=time_from,
                    time_to=time_to
                )
                db.session.add(projection)
                current_date += timedelta(days=1)

            db.session.commit()

            return Result().response()
        except Exception as e:
            db.session.rollback()
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()


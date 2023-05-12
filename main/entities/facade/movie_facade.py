import traceback
from datetime import datetime

from main.entities.core.base import db
from main.entities.facade.base_facade import BaseFacade
from main.entities.models.movie import Movie
from main.service.utility.logger import log


class MovieFacade(BaseFacade):
    def __init__(self):
        super().__init__(Movie)


    def find(self, value, column):
        try:
            movie = super().find(value, column)

            if not movie:
                return False

            old_projections_for_deletion = []
            now = datetime.now()

            for p in movie.projections:
                if p.date < now.date() or (p.date == now.date() and p.time < now.time()):
                    old_projections_for_deletion.append(p)

            for p in old_projections_for_deletion:
                movie.projections.remove(p)
                db.session.delete(p)

            db.session.commit()
            return movie

        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None





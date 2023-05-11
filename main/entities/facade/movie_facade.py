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
            log.info(f'value: {value}, column: {column}')
            movie = db.session.query(self.T).filter_by(**{column: value}).first()
            projections_to_delete = []

            if movie:
                for p in movie.projections:
                    if p.date < datetime.now().date() or (
                            p.date == datetime.now().date()
                            and p.time < datetime.now().time()
                    ):
                        log.info(f'projekcija za brisanje: {p}')
                        projections_to_delete.append(p)

                for p in projections_to_delete:
                    movie.projections.remove(p)
                    db.session.delete(p)

                db.session.commit()

                return movie

            return False
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None





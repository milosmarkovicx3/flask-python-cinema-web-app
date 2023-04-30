from entities.facade.base_facade import BaseFacade
from service.utility.logger import log
from entities.core.base import db
from entities.models.movie import Movie
from entities.models.genre import Genre
from entities.models.actor import Actor
from entities.models.movies_genres import MoviesGenres

class GenreFacade(BaseFacade):
    def __init__(self):
        super().__init__(Genre)

    def get_by_name(name):
        try:
            log.info(f'name: {name}')
            response = db.session.query(Genre).filter(Genre.name == name).first()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(e)
            return None

    def create(genre):
        try:
            log.info(f'genre: {genre}')
            if not isinstance(genre, Genre):
                return False
            db.session.add(genre)
            db.session.commit()
            return genre
        except Exception as e:
            log.error(e)
            db.rollback()
            return None



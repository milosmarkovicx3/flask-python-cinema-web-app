from entities.facade.base_facade import BaseFacade
from service.utility.logger import log
from entities.core.base import db
from entities.models.movies_actors import MoviesActors
from entities.models.movies_genres import MoviesGenres
from entities.models.movie import Movie


class MovieFacade(BaseFacade):
    def __init__(self):
        super().__init__(Movie)

    def find_by(self, id):
        try:
            log.info(f'id: {id}')
            response = db.session.query(Movie).filter(Movie.id == id).first()
            if response is None:
                return False
            else:
                return [response, response.actors, response.genres]
        except Exception as e:
            log.error(e)
            return None

    def get_by_title(title):
        try:
            log.info(f'title: {title}')
            response = db.session.query(Movie).filter(Movie.title == title).first()
            if response is None:
                return False
            else:
                return [response, response.actors, response.genres]
        except Exception as e:
            log.error(e)
            return None


    def create(movie):
        try:
            log.info(f'movie: {movie}')
            log.info(f'movie->actors: {movie.actors}')
            log.info(f'movie->genres: {movie.genres}')
            if not isinstance(movie, Movie):
                return False
            db.session.add(movie)
            db.session.commit()
            return [movie, movie.actors, movie.genres]
        except Exception as e:
            log.error(e)
            db.rollback()
            return None


from service.utility.logger import log
from entities.core.base import db
from entities.models.movie_actor import movie_actor
from entities.models.movie_genre import movie_genre
from entities.models.movies import movies

def get_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(movies).filter(movies.id == id).first()
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
        response = db.session.query(movies).filter(movies.title == title).first()
        if response is None:
            return False
        else:
            return [response, response.actors, response.genres]
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        response = db.session.query(movies).order_by(movies.title).all()
        if response is None:
            return False
        else:
            return response
    except Exception as e:
        log.error(e)
        return None

def create(movie):
    try:
        log.info(f'movie: {movie}')
        log.info(f'movie->actors: {movie.actors}')
        log.info(f'movie->genres: {movie.genres}')
        if not isinstance(movie, movies):
            return False
        db.session.add(movie)
        db.session.commit()
        return [movie, movie.actors, movie.genres]
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(movies).filter(movies.id == id).first()
        if response is None:
            return False
        db.session.delete(response)
        db.session.commit()
        return [response, response.actors, response.genres]
    except Exception as e:
        log.error(e)
        db.rollback()
        return None


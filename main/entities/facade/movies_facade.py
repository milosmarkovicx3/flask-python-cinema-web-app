from service.utility.logger import log
from entities.core.base import db
from entities.models.movie_actor import movie_actor
from entities.models.movie_genre import movie_genre
from entities.models.movies import movies
def get_by_id(id):
    try:
        log.info(f'id: {id}')
        return db.session.query(movies).filter(movies.id == id).first()
    except Exception as e:
        log.error(e)
        return None

def get_by_title(title):
    try:
        log.info(f'title: {title}')
        return db.session.query(movies).filter(movies.title == title).first()
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        return db.session.query(movies).order_by(movies.title).all()
    except Exception as e:
        log.error(e)
        return None

def create(movie,actors_with_roles, genres):
    # actors_with_roles = [{'actor': actor_1, 'role': 'Neo'}, {'actor': actor_2, 'role': 'Morpheus'}]
    # genres = [genre1, genre2]
    try:
        log.info(f'movie: {movie}')
        log.info(f'actors_with_roles: {actors_with_roles}')
        log.info(f'genres: {genres}')
        movie.actors = [movie_actor(id_actor=actor['actor'].id, role=actor['role']) for actor in actors_with_roles]
        movie.genres = [movie_genre(id_genre=genre.id) for genre in genres]
        db.session.add(movie)
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete_by_id(id):
    try:
        log.info(f'id: {id}')
        db.session.query(movies).filter_by(id = id).delete()
        db.session.query(movie_actor).filter_by(id_movie = id).delete()
        db.session.query(movie_genre).filter_by(id_movie=id).delete()
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None



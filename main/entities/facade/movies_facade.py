from log.logger import log
from ..core.base import db
from ..entities.movies import movies
from ..entities.movie_actor import movie_actor


def get_by_id(id):
    try:
        log.info(f'id: {id}')
        return db.session.query(movies).filter(movies.id == id).first()
    except Exception as e:
        log.error(e)
        return None

def get_by_title(title):
    try:
        log.info(f'id: {id}')
        return db.session.query(movies).filter(movies.title == title).first()
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        return db.session.query(movies).all()
    except Exception as e:
        log.error(e)
        return None

def create(movie,actors_with_roles):
    # actors_with_roles = [{'actor': actor_1, 'role': 'Neo'}, {'actor': actor_2, 'role': 'Morpheus'}]
    try:
        log.info(f'movie: {movie}')
        log.info(f'actors_with_roles: {actors_with_roles}')
        movie.movie_actors = [movie_actor(id_actor=actor['actor'].id, role=actor['role']) for actor in actors_with_roles]
        db.session.add(movie)
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete(id):
    try:
        log.info(f'id: {id}')
        db.session.query(movies).filter_by(id = id).delete()
        db.session.query(movie_actor).filter_by(id_movie = id).delete()
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None



from service.utility.logger import log
from entities.core.base import db
from entities.models.movies import movies
from entities.models.genres import genres
from entities.models.actors import actors
from entities.models.movie_genre import movie_genre


def get_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(genres).filter(genres.id == id).first()
        if response is None:
            return False
        else:
            return response
    except Exception as e:
        log.error(e)
        return None

def get_by_name(name):
    try:
        log.info(f'name: {name}')
        response =  db.session.query(genres).filter(genres.name == name).first()
        if response is None:
            return False
        else:
            return response
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        response =  db.session.query(genres).order_by(genres.name).all()
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
        if not isinstance(genre, genres):
            return False
        db.session.add(genre)
        db.session.commit()
        return True
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(genres).filter(genres.id == id).first()
        if response is None:
            return False
        db.session.delete(response)
        db.session.commit()
        return True
    except Exception as e:
        log.error(e)
        db.rollback()
        return None





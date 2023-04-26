from service.utility.logger import log
from entities.core.base import db
from entities.models.movies import movies
from entities.models.genres import genres
from entities.models.actors import actors
from entities.models.movie_actor import movie_actor



def get_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(actors).filter(actors.id == id).first()
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
        response = db.session.query(actors).filter(actors.name == name).first()
        if response is None:
            return False
        else:
            return response
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        response = db.session.query(actors).order_by(actors.name).all()
        if response is None:
            return False
        else:
            return response
    except Exception as e:
        log.error(e)
        return None

def create(actor):
    try:
        log.info(f'actor: {actor}')
        if not isinstance(actor, actors):
            return False
        db.session.add(actor)
        db.session.commit()
        return actor
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete_by_id(id):
    try:
        log.info(f'id: {id}')
        response = db.session.query(actors).filter(actors.id == id).first()
        if response is None:
            return False
        db.session.delete(response)
        db.session.commit()
        return response
    except Exception as e:
        log.error(e)
        db.rollback()
        return None



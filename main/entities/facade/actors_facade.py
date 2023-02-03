from log.logger import log
from ..core.base import db
from ..entities.movies import movies
from ..entities.actors import actors
from ..entities.movie_actor import movie_actor


def get_by_id(id):
    try:
        log.info(f'id: {id}')
        return db.session.query(actors).filter(actors.id == id).first()
    except Exception as e:
        log.error(e)
        return None

def get_by_name(name):
    try:
        log.info(f'id: {id}')
        return db.session.query(actors).filter(actors.name == name).first()
    except Exception as e:
        log.error(e)
        return None

def get_all():
    try:
        return db.session.query(actors).all()
    except Exception as e:
        log.error(e)
        return None

def create(actor):
    try:
        log.info(f'actor: {actor}')
        db.session.add(actor)
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None

def delete(id):
    try:
        log.info(f'id: {id}')
        db.session.query(actors).filter_by(id = id).delete()
        db.session.commit()
    except Exception as e:
        log.error(e)
        db.rollback()
        return None



from entities.facade.base_facade import BaseFacade
from service.utility.logger import log
from entities.core.base import db
from entities.models.movie import Movie
from entities.models.genre import Genre
from entities.models.actor import Actor
from entities.models.movies_actors import MoviesActors


class ActorFacade(BaseFacade):
    def __init__(self):
        super().__init__(Actor)

    def get_by_name(self, name):
        try:
            log.info(f'name: {name}')
            response = db.session.query(Actor).filter(Actor.name == name).first()
            if response is None:
                return False
            else:
                return response
        except Exception as e:
            log.error(e)
            return None

    def create(self, actor):
        try:
            log.info(f'actor: {actor}')
            if not isinstance(actor, Actor):
                return False
            db.session.add(actor)
            db.session.commit()
            return actor
        except Exception as e:
            log.error(e)
            db.rollback()
            return None



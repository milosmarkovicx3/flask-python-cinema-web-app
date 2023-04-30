from sqlalchemy import Integer, ForeignKey, String
from entities.core.base import db

MoviesActors = db.Table('movies_actors',
            db.Column('id', Integer(), primary_key=True),
            db.Column('movie_id', Integer, ForeignKey('movie.id')),
            db.Column('actor_id', Integer, ForeignKey('actor.id')),
            db.Column('role', String(255))
                       )
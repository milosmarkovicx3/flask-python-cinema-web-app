from sqlalchemy import Integer, ForeignKey, String
from ..core.base import db

movie_actor = db.Table('movie_actor',
            db.Column('id_actor', Integer, ForeignKey('actors.id'), primary_key=True),
            db.Column('id_movie', Integer, ForeignKey('movies.id'), primary_key=True),
            db.Column('role', String(255)) )



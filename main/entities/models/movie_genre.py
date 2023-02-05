from sqlalchemy import Integer, ForeignKey
from entities.core.base import db

movie_genre = db.Table('movie_genre',
            db.Column('id_movie', Integer, ForeignKey('movies.id'), primary_key=True),
            db.Column('id_genre', Integer, ForeignKey('genres.id'), primary_key=True) )



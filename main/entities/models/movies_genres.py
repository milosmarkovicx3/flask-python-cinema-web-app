from sqlalchemy import Integer, ForeignKey
from entities.core.base import db

MoviesGenres = db.Table('movies_genres',
            db.Column('id', Integer(), primary_key=True),
            db.Column('movie_id', Integer, ForeignKey('movie.id')),
            db.Column('genre_id', Integer, ForeignKey('genre.id'))
                       )


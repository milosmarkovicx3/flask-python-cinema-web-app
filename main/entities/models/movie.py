from sqlalchemy import Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
# NE BRISATI IMPORT
from main.entities.models.movies_genres import MoviesGenres
# NE BRISATI IMPORT
from main.entities.models.movies_actors import MoviesActors
from main.entities.core.base import db


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column('id', Integer, primary_key=True)
    title = db.Column('title', String(255), unique=True, nullable=False)
    year = db.Column('year', String(255), nullable=False)
    duration = db.Column('duration', String(255), nullable=False)
    rating = db.Column('rating', String(255), nullable=False)
    votes = db.Column('votes', String(255), nullable=False)
    poster = db.Column('poster', String(255), unique=True, nullable=False)
    trailer = db.Column('trailer', String(1024))

    actors_association = relationship('MoviesActors', back_populates='movie')
    actors = association_proxy('actors_association', 'actor')

    genres_association = relationship('MoviesGenres', back_populates='movie')
    genres = association_proxy('genres_association', 'genre')

    def __init__(self, title, year, duration, rating, votes, poster, trailer):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.votes = votes
        self.poster = poster
        self.trailer = trailer

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "duration": self.duration,
            "rating": self.rating,
            "votes": self.votes,
            "poster": self.poster,
            "trailer": self.trailer,
            "actors": [
                {"id": ma.actor.id,
                 "name": ma.actor.name,
                 "image": ma.actor.image,
                 "role": ma.role
                 } for ma in self.actors_association
            ],
            "genres": [
                {"id": mg.genre.id,
                 "name": mg.genre.name,
                 "image": mg.genre.image
                 } for mg in self.genres_association
            ]
        }


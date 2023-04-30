from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from entities.models.movies_actors import MoviesActors
from entities.models.movies_genres import MoviesGenres
from entities.core.base import db

class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column('id', Integer, primary_key=True)
    title = db.Column('title', String(255))
    year = db.Column('year', String(255))
    duration = db.Column('duration', String(255))
    rating = db.Column('rating', String(255))
    votes = db.Column('votes', String(255))
    poster = db.Column('poster', String(255))

    actors = relationship('Actor', secondary=MoviesActors, backref='movie')
    genres = relationship('Genre', secondary=MoviesGenres, backref='movie')

    def __init__(self, title, year, duration, rating, votes, poster):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.votes = votes
        self.poster = poster

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
            "poster": self.poster
        }




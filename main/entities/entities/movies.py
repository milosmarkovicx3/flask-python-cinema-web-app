from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from .movie_actor import movie_actor
from ..core.base import db

class movies(db.Model):
    __tablename__ = 'movies'
    id = db.Column('id', Integer, primary_key = True)
    title = db.Column('title', String(255))
    year = db.Column('year', String(255))
    duration = db.Column('duration', String(255))
    rating = db.Column('rating', String(255))
    votes = db.Column('votes', String(255))
    poster = db.Column('poster', String(255))

    #actors = relationship('actors', secondary=movie_actor, backref='movies')

    def __init__(self, title, year, duration, rating, votes, poster):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.votes = votes
        self.poster = poster

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


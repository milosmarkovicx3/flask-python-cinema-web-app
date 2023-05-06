from sqlalchemy.orm import relationship
from main.entities.core.base import db


class MoviesGenres(db.Model):
    __tablename__ = 'movies_genres'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))

    movie = relationship('Movie', back_populates='genres_association')
    genre = relationship('Genre', back_populates='movies_association')

    def __init__(self, id, movie_id, genre_id):
        self.id = id
        self.movie_id = movie_id
        self.genre_id = genre_id

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "genre_id": self.genre_id
        }
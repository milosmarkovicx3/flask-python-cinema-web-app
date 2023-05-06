from sqlalchemy.orm import relationship
from main.entities.core.base import db

class MoviesActors(db.Model):
    __tablename__ = 'movies_actors'
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actor.id'))
    role = db.Column(db.String(255))

    movie = relationship('Movie', back_populates='actors_association')
    actor = relationship('Actor', back_populates='movies_association')

    def __init__(self, id, movie_id, actor_id, role):
        self.id = id
        self.movie_id = movie_id
        self.actor_id = actor_id
        self.role = role


    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "actor_id": self.actor_id,
            "role": self.role
        }
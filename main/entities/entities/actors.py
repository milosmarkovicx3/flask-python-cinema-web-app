from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from .movie_actor import movie_actor
from ..core.base import db

class actors(db.Model):
    __tablename__ = 'actors'
    id = db.Column('id_actor', Integer, primary_key = True)
    name = db.Column('name', String(255))
    image = db.Column('image', String(255))

    movies = relationship('movies', secondary=movie_actor, backref='actors')

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
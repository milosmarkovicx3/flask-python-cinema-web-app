from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship
from entities.models.movies_actors import MoviesActors
from entities.core.base import db

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column('id', Integer, primary_key=True)
    name = db.Column('name', String(255), unique=True)
    image = db.Column('image', String(255))

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
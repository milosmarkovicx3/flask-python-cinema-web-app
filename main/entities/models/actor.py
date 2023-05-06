from sqlalchemy import Integer, String
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from main.entities.core.base import db

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column('id', Integer, primary_key=True)
    name = db.Column('name', String(255), unique=True)
    image = db.Column('image', String(255))

    movies_association = relationship('MoviesActors', back_populates='actor')
    movies = association_proxy('movies_association', 'movie')

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
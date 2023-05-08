from sqlalchemy.ext.associationproxy import association_proxy

from main.entities.core.base import db

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), unique=True)
    image = db.Column('image', db.String(255), unique=True)

    movies_association = db.relationship('MoviesGenres', back_populates='genre')
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
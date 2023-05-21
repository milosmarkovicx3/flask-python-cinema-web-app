from sqlalchemy.ext.associationproxy import association_proxy
from main.entities.core.base import db

class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    image = db.Column('image', db.String(64), unique=True)

    movies_association = db.relationship('MoviesGenres', back_populates='genre')
    movies = association_proxy('movies_association', 'movie')

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __str__(self):
        return f'Genre(id={self.id}, name={self.name})'

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
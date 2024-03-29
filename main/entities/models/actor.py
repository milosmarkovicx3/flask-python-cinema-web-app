from sqlalchemy.ext.associationproxy import association_proxy
from main.entities.core.base import db

class Actor(db.Model):
    __tablename__ = 'actor'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), unique=True)
    image = db.Column('image', db.String(64))

    movies_association = db.relationship('Role', back_populates='actor')
    movies = association_proxy('movies_association', 'movie')

    def __init__(self, name, image):
        self.name = name
        self.image = image

    def __str__(self):
        return f'Actor(id={self.id}, name={self.name})'

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "image": self.image
        }
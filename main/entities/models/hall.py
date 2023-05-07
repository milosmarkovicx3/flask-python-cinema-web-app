from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from main.entities.core.base import db

class Hall(db.Model):
    __tablename__ = 'hall'
    id = db.Column('id', Integer, primary_key=True)
    name = db.Column('name', String(255), nullable=False)
    capacity = db.Column('capacity', Integer, nullable=False)

    seats = relationship('Seat', backref='hall')

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity
        }
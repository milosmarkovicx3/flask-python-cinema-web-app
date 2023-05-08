from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship

from main.entities.core.base import db

class SeatType(db.Model):
    __tablename__ = 'seat_type'
    id = db.Column('id', Integer, primary_key=True)
    type = db.Column('type', String(255), nullable=False)

    seats = relationship('Seat', backref='seat_type')

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "type": self.type
        }
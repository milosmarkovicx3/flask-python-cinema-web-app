from datetime import datetime
from main.entities.core.base import db

class Reservation(db.Model):
    SEAT_TYPE = 6
    __tablename__ = 'reservation'
    id = db.Column('id', db.Integer, primary_key=True)
    projection_id = db.Column('projection_id', db.Integer, db.ForeignKey('projection.id'), nullable=False)
    seat_id = db.Column('seat_id', db.Integer, db.ForeignKey('seat.id'), nullable=False)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column('created_at', db.DateTime(), nullable=False)

    def __init__(self, projection_id, seat_id, user_id):
        self.projection_id = projection_id
        self.seat_id = seat_id
        self.user_id = user_id
        self.created_at = datetime.now()

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "projection_id": self.projection_id,
            "seat_id": self.seat_id,
            "user_id": self.user_id,
            "created_at": str(self.created_at)
        }
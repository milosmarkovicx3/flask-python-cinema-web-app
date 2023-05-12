from datetime import datetime
from main.entities.core.base import db

class Reservation(db.Model):
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
            "projection": {
                "date": self.projection.date.strftime('%d.%m.%Y'),
                "time": self.projection.time.strftime('%H:%M'),
                "movie_title": self.projection.movie.title,
                "movie_year": self.projection.movie.year,
                "movie_poster": self.projection.movie.poster
            },
            "seat": {
                "row": self.seat.row,
                "number": self.check_love_seat()
            },
            "user_id": self.user_id,
            "created_at": self.created_at.strftime('%d.%m.%Y, %H:%M')
        }

    def check_love_seat(self):
        if self.seat.seat_type.type == 'love_left':
            return self.seat_id


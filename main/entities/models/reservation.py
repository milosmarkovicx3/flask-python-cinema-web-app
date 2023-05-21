from datetime import datetime
from main.entities.core.base import db
from main.service.utility.utils import repr_format_date, repr_format_time


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
        return f'Reservation(id={self.id})'

    def __repr__(self):
        return {
            "id": self.id,
            "projection": {
                "date": repr_format_date(self.projection.date),
                "time": repr_format_time(self.projection.time),
                "movie_title": self.projection.movie.title,
                "movie_year": self.projection.movie.year,
                "movie_poster": self.projection.movie.poster
            },
            "seat": {
                "row": self.seat.row,
                "number": self.seat.number
            },
            "user_id": self.user_id,
            "created_at": self.created_at.strftime('%d.%m.%Y, %H:%M')
        }




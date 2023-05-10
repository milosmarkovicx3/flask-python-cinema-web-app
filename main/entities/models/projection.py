from main.entities.core.base import db
from main.entities.models.reservation import Reservation


class Projection(db.Model):
    __tablename__ = 'projection'
    id = db.Column('id', db.Integer, primary_key=True)
    hall_id = db.Column('hall_id', db.Integer, db.ForeignKey('hall.id'), nullable=False)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), nullable=False)
    date_from = db.Column('date_from', db.Date(), nullable=False)
    date_to = db.Column('date_to', db.Date(), nullable=False)
    time = db.Column('time', db.Time(), nullable=False)

    reservations = db.relationship('Reservation', backref='projection')

    def __init__(self, hall_id, movie_id, date_from, date_to, time):
        self.hall_id = hall_id
        self.movie_id = movie_id
        self.date_from = date_from
        self.date_to = date_to
        self.time = time

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "hall_id": self.hall_id,
            "movie_id": self.movie_id,
            "date_from": self.date_from.strftime('%d.%m.%Y'),
            "date_to": self.date_to.strftime('%d.%m.%Y'),
            "time": str(self.time)[:5],
            "seats": self.get_seats_for_projection()

        }

    def get_seats_for_projection(self):
        seats = []
        reservations = [reservation.id for reservation in self.reservations]
        for seat in self.hall.seats:
            if seat.id in reservations:
                seats.append([seat.row, seat.number, Reservation.SEAT_TYPE])
            else:
                seats.append([seat.row, seat.number, seat.seat_type_id])

        return seats












import math
import re
from main.entities.core.base import db
from main.entities.facade.seat_type_facade import SeatTypeFacade
from main.service.utility.utils import repr_format_time, repr_format_date

class Projection(db.Model):
    __tablename__ = 'projection'
    id = db.Column('id', db.Integer, primary_key=True)
    hall_id = db.Column('hall_id', db.Integer, db.ForeignKey('hall.id'), nullable=False)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), nullable=False)
    date = db.Column('date', db.Date(), nullable=False)
    time_from = db.Column('time_from', db.Time(), nullable=False)
    time_to = db.Column('time_to', db.Time(), nullable=False)

    reservations = db.relationship('Reservation', backref='projection')

    def __init__(self, hall_id, movie_id, date, time_from, time_to):
        self.hall_id = hall_id
        self.movie_id = movie_id
        self.date = date
        self.time_from = time_from
        self.time_to = time_to

    def __str__(self):
        return f'Projection(id={self.id}, date={self.date}, time_from={self.time_from}, time_to={self.time_to})'

    def __repr__(self):
        return {
            "id": self.id,
            "hall_id": self.hall_id,
            "hall_name": self.hall.name,
            "movie_id": self.movie_id,
            "date": repr_format_date(self.date),
            "time_from": repr_format_time(self.time_from),
            "time_to": repr_format_time(self.time_to),
            "seats": self.get_seats_for_projection()
        }

    def get_seats_for_projection(self):
        seats = []
        reservations = [reservation.seat_id for reservation in self.reservations]
        stf = SeatTypeFacade()
        reserved_type = stf.find(column='type', value='reserved')
        if not reserved_type:
            return
        for seat in self.hall.seats:
            if seat.id in reservations:
                seats.append({
                    "id": seat.id,
                    "row": seat.row,
                    "number": seat.number,
                    "type": reserved_type.id,
                    "image": reserved_type.image,
                    "love": False if seat.seat_type_id != 5 else True
                })
            else:
                seats.append({
                    "id": seat.id,
                    "row": seat.row,
                    "number": seat.number,
                    "type": seat.seat_type_id,
                    "image": seat.seat_type.image,
                    "ticket_price": self.ticket_price(seat.seat_type_id)
                })

        return seats

    def ticket_price(self, seat_type):
        first_number = int(re.findall(r'\d+', self.movie.duration)[0])
        price = 200 + first_number * 100

        if seat_type == 2:
            price = int(round(price * 1.2))
        elif seat_type == 5:
            price = int(round(price * 2))

        if self.date.weekday() == 1:
            return int(math.ceil(price*0.8 / 10) * 10)

        if seat_type == 5:
            return f'2x{price}rsd'
        else:
            return f'1x{price}rsd'











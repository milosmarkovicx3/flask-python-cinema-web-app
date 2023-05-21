from main.entities.core.base import db

class Seat(db.Model):
    __tablename__ = 'seat'
    id = db.Column('id', db.Integer, primary_key=True)
    hall_id = db.Column('hall_id', db.Integer, db.ForeignKey('hall.id'), nullable=False)
    seat_type_id = db.Column('seat_type_id', db.Integer, db.ForeignKey('seat_type.id'), nullable=False)
    row = db.Column('row', db.Integer, nullable=False)
    number = db.Column('number', db.String(8), nullable=False)

    reservations = db.relationship('Reservation', backref='seat')

    def __init__(self, hall_id, seat_type_id, row, number):
        self.hall_id = hall_id
        self.seat_type_id = seat_type_id
        self.row = row
        self.number = number

    def __str__(self):
        return f'Seat(id={self.id})'

    def __repr__(self):
        return {
            "id": self.id,
            "hall_id": self.hall_id,
            "seat_type_id": self.seat_type_id,
            "row": self.row,
            "number": self.number
        }
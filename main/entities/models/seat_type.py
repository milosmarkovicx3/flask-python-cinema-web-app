from main.entities.core.base import db

class SeatType(db.Model):
    __tablename__ = 'seat_type'
    id = db.Column('id', db.Integer, primary_key=True)
    type = db.Column('type', db.String(64), nullable=False)
    image = db.Column('image', db.String(64), nullable=False)

    seats = db.relationship('Seat', backref='seat_type')

    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'SeatType(id={self.id}, type={self.type})'

    def __repr__(self):
        return {
            "id": self.id,
            "type": self.type,
            "image": self.image
        }
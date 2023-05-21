from main.entities.core.base import db
# -NE-BRISATI-IMPORT------------------------------------------
from main.entities.models.seat import Seat
# ------------------------------------------------------------

class Hall(db.Model):
    __tablename__ = 'hall'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(64), nullable=False)
    capacity = db.Column('capacity', db.Integer, nullable=False)

    seats = db.relationship('Seat', backref='hall')
    projections = db.relationship('Projection', backref='hall')

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

    def __str__(self):
        return f'Hall(id={self.id}, name={self.name})'

    def __repr__(self):
        return {
            "id": self.id,
            "name": self.name,
            "capacity": self.capacity
        }
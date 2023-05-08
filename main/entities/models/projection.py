from main.entities.core.base import db

class Projection(db.Model):
    __tablename__ = 'projection'
    id = db.Column('id', db.Integer, primary_key=True)
    hall_id = db.Column('hall_id', db.Integer, db.ForeignKey('hall.id'), nullable=False)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), nullable=False)
    date_from = db.Column('date_from', db.Date(), nullable=False)
    date_to = db.Column('date_to', db.Date(), nullable=False)
    time = db.Column('time', db.Time(), nullable=False)

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
            "date_from": str(self.date_from),
            "date_to": str(self.date_to),
            "time": str(self.time)
        }
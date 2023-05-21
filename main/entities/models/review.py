from datetime import datetime
from main.entities.core.base import db
from main.service.utility.utils import repr_format_date


class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), nullable=False)
    comment = db.Column('comment', db.String(2048))
    rating = db.Column('rating', db.Integer)
    created_at = db.Column('created_at', db.Date(), nullable=False)

    movie = db.relationship('Movie', back_populates='reviews_association')
    user = db.relationship('User', back_populates='reviews_association')

    def __init__(self, movie_id, user_id, comment, rating):
        self.movie_id = movie_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating
        self.created_at = datetime.now().date()

    def __str__(self):
        return f'Review(id={self.id})'

    def __repr__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": repr_format_date(self.created_at)
        }
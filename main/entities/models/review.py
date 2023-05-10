from main.entities.core.base import db

class Review(db.Model):
    __tablename__ = 'review'
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), nullable=False)
    comment = db.Column('comment', db.String(1024))
    rating = db.Column('rating', db.Integer)
    created_at = db.Column('created_at', db.Date(), nullable=False)

    movie = db.relationship('Movie', back_populates='reviews_association')
    user = db.relationship('User', back_populates='reviews_association')

    def __init__(self, movie_id, user_id, comment, rating, created_at):
        self.movie_id = movie_id
        self.user_id = user_id
        self.comment = comment
        self.rating = rating
        self.created_at = created_at

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": str(self.created_at)
        }
from sqlalchemy.ext.associationproxy import association_proxy
from main.entities.core.base import db
# -NE-BRISATI-IMPORTE------------------------------------------
from main.entities.models.movies_genres import MoviesGenres
from main.entities.models.movies_actors import MoviesActors
from main.entities.models.movies_reviews import MoviesReviews
# -------------------------------------------------------------


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column('id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(255), unique=True, nullable=False)
    year = db.Column('year', db.Integer, nullable=False)
    duration = db.Column('duration', db.String(255), nullable=False)
    rating = db.Column('rating', db.String(255), nullable=False)
    votes = db.Column('votes', db.Integer, nullable=False)
    poster = db.Column('poster', db.String(255), unique=True, nullable=False)
    trailer = db.Column('trailer', db.String(1024))

    """
    relationship - many to many preko klasa
    :param 1: Naziv vezne klase.
    :param 2: Naziv promenljive u veznoj klasi za tu vezu.
    
    association_proxy
    :param 1: Naziv promenljive u trenutnoj klasi preko koje smo povezani sa veznom klasom.
    :param 2: Naziv promenljive u veznoj klasi koja predstavlja direktu vezu sa drugu klasom.
    """
    actors_association = db.relationship('MoviesActors', back_populates='movie')
    actors = association_proxy('actors_association', 'actor')

    genres_association = db.relationship('MoviesGenres', back_populates='movie')
    genres = association_proxy('genres_association', 'genre')

    users_reviews_association = db.relationship('MoviesReviews', back_populates='movie')
    users_reviews = association_proxy('users_reviews_association', 'user')

    """
    Ovaj vid spajanja klasa zahteva deklaraciju samo u parent klasi.
    relationship - one to many preko stranog ključa
    :param 1: Naziv dečije klase koja sadrži strani ključ.
    :param 2: Referenca (kao vid promenljive) preko koje dete klasa može da pristupi parent klasi.
    """
    projections = db.relationship('Projection', backref='movie')

    def __init__(self, title, year, duration, rating, votes, poster, trailer):
        self.title = title
        self.year = year
        self.duration = duration
        self.rating = rating
        self.votes = votes
        self.poster = poster
        self.trailer = trailer

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "title": self.title,
            "year": self.year,
            "duration": self.duration,
            "rating": self.rating,
            "votes": self.votes,
            "poster": self.poster,
            "trailer": self.trailer,
            "actors": [
                {"id": ma.actor.id,
                 "name": ma.actor.name,
                 "image": ma.actor.image,
                 "role": ma.role
                 } for ma in self.actors_association
            ],
            "genres": [
                {"id": mg.genre.id,
                 "name": mg.genre.name,
                 "image": mg.genre.image
                 } for mg in self.genres_association
            ],
            "projections": [
                {"date_from": str(p.date_from),
                 "date_to": str(p.date_to),
                 "time": str(p.time),
                 "hall_name": p.hall.name
                 } for p in self.projections
            ],
            "users_reviews": [
                {"user_id": mur.user.username,
                 "comment": mur.comment,
                 "rating": mur.rating,
                 "created_at": str(mur.created_at)
                 } for mur in self.users_reviews_association
            ]
        }

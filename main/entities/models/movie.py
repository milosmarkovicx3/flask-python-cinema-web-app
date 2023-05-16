from datetime import datetime, timedelta
from sqlalchemy.ext.associationproxy import association_proxy
from main.entities.core.base import db
# -NE-BRISATI-IMPORTE------------------------------------------
from main.entities.models.movies_genres import MoviesGenres
from main.entities.models.role import Role
from main.entities.models.review import Review
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
    actors_association = db.relationship('Role', back_populates='movie')
    actors = association_proxy('actors_association', 'actor')

    genres_association = db.relationship('MoviesGenres', back_populates='movie')
    genres = association_proxy('genres_association', 'genre')

    reviews_association = db.relationship('Review', back_populates='movie')
    reviews = association_proxy('reviews_association', 'user')

    """
    Ovaj vid spajanja klasa zahteva deklaraciju samo u parent klasi.
    relationship - one to many preko stranog ključa
    :param 1: Naziv dečije klase koja sadrži strani ključ.
    :param 2: Naziv tabele u kojoj se trenutno nalazimo.
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
            "votes": self.format_vote_count(),
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
            "projections": self.projections_for_next_week(),
            "reviews": [
                {"user_username": mur.user.username,
                 "user_image": mur.user.image,
                 "comment": mur.comment,
                 "rating": mur.rating,
                 "created_at": mur.created_at.strftime('%d.%m.%Y')
                 } for mur in self.reviews_association
            ]
        }

    def format_vote_count(self):
        if self.votes >= 1000000:
            return '{}M'.format(round(self.votes / 1000000))
        else:
            return '{}K'.format(round(self.votes / 1000))

    def projections_for_next_week(self):
        today = datetime.now().date()
        five_days_from_today = today + timedelta(days=4)

        day_name = {0: 'PONEDELJAK', 1: 'UTORAK', 2: 'SREDA', 3: 'ČETVRTAK', 4: 'PETAK', 5: 'SUBOTA', 6: 'NEDELJA'}
        _list = {}

        for projection in self.projections:
            date = projection.date
            time = projection.time

            if date > five_days_from_today or (date == today and time < datetime.now().time()):
                continue

            day_index = date.weekday()
            key = date.strftime('%d.%m.%Y')
            if key not in _list:
                _list[key] = {
                    "day_name": "",
                    "hall_time": []
                }
                if date == today:
                    _list[key]["day_name"] = f'DANAS, {day_name[day_index][:3]}'
                elif date == today + timedelta(days=1):
                    _list[key]["day_name"] = f'SUTRA, {day_name[day_index][:3]}'
                else:
                    _list[key]["day_name"] = day_name[day_index]

            _list[key]["hall_time"].append({
                "id": projection.id,
                "hall_name": projection.hall.name,
                "time": time.strftime('%H:%M')
            })

        for day in _list:
            _list[day]["hall_time"] = sorted(_list[day]["hall_time"], key=lambda x: x["time"])

        return _list












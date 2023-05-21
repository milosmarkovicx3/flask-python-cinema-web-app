import os
from json import loads
from sqlalchemy import or_
from werkzeug.utils import secure_filename
from config import STATIC_DIR_PATH
from main.entities.core.base import db
from main.entities.core.status import Status
from main.entities.models.actor import Actor
from main.entities.models.genre import Genre
from main.entities.models.movie import Movie
from main.entities.facade.movie_facade import MovieFacade
from main.entities.core.result import Result, result_handler
from main.entities.models.role import Role
from main.entities.models.movies_genres import MoviesGenres
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log


class MovieImpl(BaseImpl):
    def __init__(self):
        super().__init__(MovieFacade)

    def create(self, form, files):
        filename, movie = '', ''
        try:
            title = form.get('title')
            year = form.get('year')
            duration = form.get('duration')
            rating = form.get('rating')
            votes = form.get('votes')
            poster = files.get('poster')
            trailer = form.get('trailer')

            # vrednosti dobijaju kao json string, iako kada se uradi print() prikazuje običan string
            actors = loads(form.get('actors'))
            genres = loads(form.get('genres'))

            filename = secure_filename(poster.filename)
            poster.save(os.path.join(f'{STATIC_DIR_PATH}/resources/movie-posters', filename))

            movie = Movie(
                title=title,
                year=year,
                duration=duration,
                rating=rating,
                votes=votes,
                poster=poster.filename,
                trailer=trailer
            )

            db.session.add(movie)
            db.session.commit()

            for actor in actors:
                ma = Role(movie_id=movie.id, actor_id=actor[0], role=actor[1])
                db.session.add(ma)

            for genre in genres:
                mg = MoviesGenres(movie_id=movie.id, genre_id=genre[0])
                db.session.add(mg)

            db.session.commit()

            return result_handler(item=movie)
        except Exception as e:
            if movie and movie.id:
                db.session.delete(movie)
                db.session.commit()
            db.session.rollback()
            os.remove(os.path.join(f'{STATIC_DIR_PATH}/resources/movie-posters', filename))
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()

    def repertoire(self, imdb_rating=None, timeline=None, genre_name=None, search_input=None, sort_method=None, page=1, per_page=12):
        try:
            query = db.session.query(Movie)

            if imdb_rating is not None:
                query = query.filter(Movie.rating >= imdb_rating)

            if timeline is not None:
                timeline = int(timeline)
                query = query.filter(Movie.year.between(timeline, timeline + 10))

            if genre_name is not None:
                query = query.filter(Movie.genres.any(Genre.name == genre_name))

            if search_input is not None:
                query = query.filter(or_(
                    Movie.title.like(f'%{search_input}%'),
                    Movie.year.like(f'%{search_input}%'),
                    Movie.actors.any(Actor.name.like(f'%{search_input}%'))
                ))

            if sort_method is not None:
                sort_map = {
                    'title_asc': Movie.title.asc(),
                    'title_desc': Movie.title.desc(),
                    'year_asc': Movie.year.asc(),
                    'year_desc': Movie.year.desc(),
                    'rating_asc': Movie.rating.asc(),
                    'rating_desc': Movie.rating.desc(),
                    'votes_asc': Movie.votes.asc(),
                    'votes_desc': Movie.votes.desc(),
                }
                if sort_method in sort_map:
                    query = query.order_by(sort_map[sort_method])

            movies = query.paginate(page=int(page), per_page=int(per_page), error_out=False)
            return movies
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return None

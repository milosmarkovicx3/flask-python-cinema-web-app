import os
import traceback
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
from main.entities.core.result import Result
from main.entities.models.movies_actors import MoviesActors
from main.entities.models.movies_genres import MoviesGenres
from main.service.impl.base_impl import BaseImpl, _result_handler
from main.service.utility.logger import log


class MovieImpl(BaseImpl):
    def __init__(self):
        super().__init__(MovieFacade)


    def create(self, data, files):
        filename, movie = '', ''
        try:
            title = data['title']
            year = data['year']
            duration = data['duration']
            rating = data['rating']
            votes = data['votes']
            poster = files['poster']
            trailer = data['trailer']

            # jer se dobija kao json string iako kada se uradi log sve prikazuje lepo
            actors = loads(data['actors'])
            genres = loads(data['genres'])

            if poster:
                filename = secure_filename(poster.filename)
                poster.save(os.path.join(f'{STATIC_DIR_PATH}\\resources\\movie-posters\\', filename))
            else:
                result = Result(status=Status.BAD_REQUEST, description='Došlo je do greške prilikom optremanja postera.')
                return result.response()

            movie = Movie(title=title, year=year, duration=duration, rating=rating, votes=votes, poster=poster.filename, trailer=trailer )

            db.session.add(movie)
            db.session.commit()

            for actor in actors:
                ma = MoviesActors(movie_id=movie.id, actor_id=actor[0], role=actor[1])
                db.session.add(ma)

            for genre in genres:
                mg = MoviesGenres(movie_id=movie.id, genre_id=genre[0])
                db.session.add(mg)

            db.session.commit()

            return _result_handler(item=movie)
        except Exception as e:
            db.session.rollback()
            db.session.delete(movie)
            db.session.commit()
            os.remove(os.path.join(f'{STATIC_DIR_PATH}\\resources\\movie-posters\\', filename))
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()

    def repertoire_search(self, kwargs):
        try:
            query = db.session.query(Movie)

            if 'imdb_rating' in kwargs and kwargs['imdb_rating'] != '':
                imdb_rating = kwargs['imdb_rating']
                query = query.filter(Movie.rating >= imdb_rating)

            if 'timeline' in kwargs and kwargs['timeline'] != '':
                timeline = int(kwargs['timeline'])
                query = query.filter(Movie.year.between(timeline, timeline + 10))

            if 'genre_name' in kwargs and kwargs['genre_name'] != '':
                genre_name = kwargs['genre_name']
                query = query.filter(Movie.genres.any(Genre.name == genre_name))

            if 'search_input' in kwargs and kwargs['search_input'] != '':
                search_input = kwargs['search_input']
                query = query.filter(or_(
                    Movie.title.like(f'%{search_input}%'),
                    Movie.year.like(f'%{search_input}%'),
                    Movie.genres.any(Genre.name.like(f'%{search_input}%')),
                    Movie.actors.any(Actor.name.like(f'%{search_input}%'))
                ))

            if 'sort_method' in kwargs and kwargs['sort_method'] != '':
                sort_method = kwargs['sort_method']
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

            page = int(kwargs['page']) if 'page' in kwargs and kwargs['page'] != '' else 1
            per_page = int(kwargs['per_page']) if 'per_page' in kwargs and kwargs['per_page'] != '' else 12

            movies = query.paginate(page=page, per_page=per_page, error_out=False)

            return movies
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

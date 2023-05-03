import traceback

from sqlalchemy import or_

from entities.facade.base_facade import BaseFacade
from entities.models.actor import Actor
from entities.models.genre import Genre
from service.utility.logger import log
from entities.core.base import db
from entities.models.movies_actors import MoviesActors
from entities.models.movies_genres import MoviesGenres
from entities.models.movie import Movie


class MovieFacade(BaseFacade):
    def __init__(self):
        super().__init__(Movie)

    def find(self, value, column):
        response = super().find(value, column)
        if response:
            return [response, response.actors, response.genres]
        return response

    def create(movie):
        try:
            log.info(f'movie: {movie}')
            log.info(f'movie->actors: {movie.actors}')
            log.info(f'movie->genres: {movie.genres}')
            if not isinstance(movie, Movie):
                return False
            db.session.add(movie)
            db.session.commit()
            return [movie, movie.actors, movie.genres]
        except Exception as e:
            log.error(e)
            db.rollback()
            return None

    def repertoire_search(self, search_input, imdb_rating, timeline, genre_name, sort_method, page, per_page):
        try:
            query = db.session.query(Movie)

            if imdb_rating is not None:
                query = query.filter(Movie.rating >= imdb_rating)

            if timeline is not None:
                query = query.filter(Movie.year.between(timeline, timeline + 10))

            if genre_name is not None:
                query = query.filter(Movie.genres.any(Genre.name == genre_name))

            if search_input is not None:
                query = query.filter(or_(
                    Movie.title.like(f'%{search_input}%'),
                    Movie.year.like(f'%{search_input}%'),
                    Movie.genres.any(Genre.name.like(f'%{search_input}%')),
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

            movies = query.paginate(page=page, per_page=per_page, error_out=False)

            return movies
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return None

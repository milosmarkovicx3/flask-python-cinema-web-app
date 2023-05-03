import os

from flask import session
from werkzeug.utils import secure_filename

from entities.core.status import Status
from entities.facade.movie_facade import MovieFacade
from service.impl.base_impl import BaseImpl, __result_handler__
from service.utility.logger import log, project_path
from service.utility.utils import json
from entities.core.result import Result
from entities.facade import movie_facade as mf
from entities.models.movie import Movie
from service.core.wtf_forms import wtf_create_movie


class MovieImpl(BaseImpl):
    def __init__(self):
        super().__init__(MovieFacade)

    def create(data):
        try:
            result = Result()
            form = wtf_create_movie()
            if not form.validate():
                result.set_status(Status.BAD_REQUEST)
                return json(result)

            image_file = data['actorFile']
            filename = secure_filename(image_file.filename)
            upload_folder = f'{project_path}static/resources/movies-images/'
            image_file.save(os.path.join(upload_folder, filename))

            movie = Movie(name=data['name'], image=data['image'])
            # actors_with_roles = [{'actor': actor_1, 'role': 'Neo'}, {'actor': actor_2, 'role': 'Morpheus'}]
            # genres = [genre1, genre2]
            # movie.actors = [movie_actor(id_actor=actor['actor'].id, role=actor['role']) for actor in actors_with_roles]
            # movie.genres = [movie_genre(id_genre=genre.id) for genre in genres]
            result.set_item(mf.create(movie))

            if result.get_item() is False:
                result.set_status(Status.BAD_REQUEST)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(e)
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)

    def repertoire_search(self, search_input, imdb_rating, timeline, genre_name, sort_method, page, per_page):
        search_input = search_input if search_input else None
        imdb_rating = imdb_rating if imdb_rating else None
        timeline = int(timeline) if timeline else None
        genre_name = genre_name if genre_name else None
        sort_method = sort_method if sort_method else None
        page = int(page) if page else 1
        per_page = int(per_page) if per_page else 20

        return self.T.repertoire_search(search_input, imdb_rating, timeline, genre_name, sort_method, page, per_page)

import os
from werkzeug.utils import secure_filename
from service.utility.logger import log, project_path
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import movies_facade as mf
from entities.models.movies import movies
from service.core.wtf_forms import wtf_create_movie

def get_by_id(id):
    try:
        result = Result(item = mf.get_by_id(id))
        if result.get_item() is False:
            result.set_status_with_description(Result.NOT_FOUND)
        elif result.get_item() is None:
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        result = Result()
        result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)

def get_by_title(title):
    try:
        result = Result(item = mf.get_by_title(title))
        if result.get_item() is False:
            result.set_status_with_description(Result.NOT_FOUND)
        elif result.get_item() is None:
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        result = Result()
        result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)

def get_all():
    try:
        result = Result(item = mf.get_all())
        if result.get_item() is False:
            result.set_status_with_description(Result.NOT_FOUND)
        elif result.get_item() is None:
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        result = Result()
        result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)

def create(data):
    try:
        result = Result()
        form =  wtf_create_movie()
        if not form.validate():
            result.set_status_with_description(Result.BAD_REQUEST)
            return toJSON(result)

        image_file = data['actorFile']
        filename = secure_filename(image_file.filename)
        upload_folder = f'{project_path}static/resources/movies-images/'
        image_file.save(os.path.join(upload_folder, filename))

        movie = movies(name = data['name'], image = data['image'])
        # actors_with_roles = [{'actor': actor_1, 'role': 'Neo'}, {'actor': actor_2, 'role': 'Morpheus'}]
        # genres = [genre1, genre2]
        # movie.actors = [movie_actor(id_actor=actor['actor'].id, role=actor['role']) for actor in actors_with_roles]
        # movie.genres = [movie_genre(id_genre=genre.id) for genre in genres]
        result.set_item(mf.create(movie))

        if result.get_item() is False:
            result.set_status_with_description(Result.BAD_REQUEST)
        elif result.get_item() is None:
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        result = Result()
        result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)

def delete_by_id(id):
    try:
        result = Result(item = mf.delete_by_id(id))
        if result.get_item() is False:
            result.set_status_with_description(Result.NOT_FOUND)
        elif result.get_item() is None:
            result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        result = Result()
        result.set_status_with_description(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
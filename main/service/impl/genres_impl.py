import os
from werkzeug.utils import secure_filename
from service.utility.logger import log, project_path
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import genres_facade as gf
from entities.models.genres import genres
from service.core.wtf_forms import wtf_create_genre

def get_by_id(id):
    try:
        result = Result(item = gf.get_by_id(id))
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

def get_by_name(name):
    try:
        result = Result(item = gf.get_by_name(name))
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
        result = Result(item = gf.get_all())
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
        form =  wtf_create_genre()
        if not form.validate():
            result.set_status_with_description(Result.BAD_REQUEST)
            return toJSON(result)

        image_file = data['actorFile']
        filename = secure_filename(image_file.filename)
        upload_folder = f'{project_path}static/resources/genres-images/'
        image_file.save(os.path.join(upload_folder, filename))

        genre = genres(name = data['name'], image = data['image'])
        result.set_item(gf.create(genre))

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
        result = Result(item = gf.delete_by_id(id))
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
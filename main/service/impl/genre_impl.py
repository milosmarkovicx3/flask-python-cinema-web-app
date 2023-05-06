import os
from werkzeug.utils import secure_filename
from main.entities.core.status import Status
from main.entities.facade import genre_facade as gf
from main.entities.models.genre import Genre
from main.entities.facade.genre_facade import GenreFacade
from main.entities.core.result import Result
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log
from main.service.utility.utils import json

class GenreImpl(BaseImpl):
    def __init__(self):
        super().__init__(GenreFacade)


    def create(self, data):
        try:
            result = Result()
            form =  wtf_create_genre()
            if not form.validate():
                result.set_status(Status.BAD_REQUEST)
                return json(result)

            image_file = data['actorFile']
            filename = secure_filename(image_file.filename)
            upload_folder = f'{project_path}static/resources/genres-images/'
            image_file.save(os.path.join(upload_folder, filename))

            genre = Genre(name = data['name'], image = data['image'])
            result.set_item(gf.create(genre))

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

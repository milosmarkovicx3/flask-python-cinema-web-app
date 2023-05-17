import os
import traceback
from werkzeug.utils import secure_filename
from config import STATIC_DIR_PATH
from main.entities.core.status import Status
from main.entities.models.genre import Genre
from main.entities.facade.genre_facade import GenreFacade
from main.entities.core.result import Result, result_handler
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log

class GenreImpl(BaseImpl):
    def __init__(self):
        super().__init__(GenreFacade)

    def create(self, data, files):
        filename = ''
        try:
            name = data['genre-name']
            image = files['genre-image']

            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(f'{STATIC_DIR_PATH}\\resources\\genre-images\\', filename))
            else:
                result = Result(
                    status=Status.BAD_REQUEST,
                    description='Error: došlo je do greške prilikom optremanja slike.'
                )
                return result.response()

            genre = Genre(name=name, image=image.filename)
            return result_handler(item=self.T.create(genre))
        except Exception as e:
            os.remove(os.path.join(f'{STATIC_DIR_PATH}\\resources\\genre-images\\', filename))
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


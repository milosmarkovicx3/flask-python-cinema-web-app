import os
import traceback
from werkzeug.utils import secure_filename
from config import STATIC_DIR_PATH
from main.entities.core.status import Status
from main.entities.models.actor import Actor
from main.entities.facade.actor_facade import ActorFacade
from main.entities.core.result import Result, result_handler
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log


class ActorImpl(BaseImpl):
    def __init__(self):
        super().__init__(ActorFacade)

    def create(self, data, files):
        filename = ''
        try:
            name = data['actor-name']
            image = files['actor-image']

            if image:
                filename = secure_filename(image.filename)
                image.save(os.path.join(f'{STATIC_DIR_PATH}\\resources\\actor-images\\', filename))
            else:
                result = Result(
                    status=Status.BAD_REQUEST,
                    description='\nError: došlo je do greške prilikom optremanja slike.'
                )
                return result.response()

            actor = Actor(name=name, image=image.filename)
            return result_handler(item=self.T.create(actor))
        except Exception as e:
            os.remove(os.path.join(f'{STATIC_DIR_PATH}\\resources\\actor-images\\', filename))
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


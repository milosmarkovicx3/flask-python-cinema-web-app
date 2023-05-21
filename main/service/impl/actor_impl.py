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

    def create(self, form, files):
        filename = ''
        try:
            name = form.get('actor-name')
            image = files.get('actor-image')

            filename = secure_filename(image.filename)
            image.save(os.path.join(f'{STATIC_DIR_PATH}/resources/actor-images', filename))

            actor = Actor(name=name, image=image.filename)
            return result_handler(item=self.T.create(actor))
        except Exception as e:
            os.remove(os.path.join(f'{STATIC_DIR_PATH}/resources/actor-images', filename))
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()


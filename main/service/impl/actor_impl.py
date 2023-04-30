import os
from werkzeug.utils import secure_filename

from entities.facade.actor_facade import ActorFacade
from service.impl.base_impl import BaseImpl
from service.utility.logger import log, project_path
from service.utility.utility import json
from entities.core.result import Result
from entities.facade import actor_facade as af
from entities.models.actor import Actor
from service.core.wtf_forms import wtf_create_actor


class ActorImpl(BaseImpl):
    def __init__(self):
        super().__init__(ActorFacade)

    def get_by_name(self, name):
        try:
            result = Result(item=self.T.get_by_name(name))
            if result.get_item() is False:
                result.set_status(Result.NOT_FOUND)
            elif result.get_item() is None:
                result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)
        except Exception as e:
            log.error(e)
            result = Result()
            result.set_status(Status.INTERNAL_SERVER_ERROR)
            return json(result)


    def create(self, data):
        try:
            result = Result()
            form =  wtf_create_actor()
            if not form.validate():
                result.set_status(Status.BAD_REQUEST)
                return json(result)

            image_file = data['actorFile']
            filename = secure_filename(image_file.filename)
            upload_folder = f'{project_path}static/resources/actors-images/'
            image_file.save(os.path.join(upload_folder, filename))

            actor = Actor(name=data['name'], image=data['image'])
            result.set_item(self.T.create(actor))

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


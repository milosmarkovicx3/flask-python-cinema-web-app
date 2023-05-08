import traceback

from main.entities.core.result import Result
from main.entities.core.status import Status
from main.entities.facade.projection_facade import ProjectionFacade
from main.entities.models.projection import Projection
from main.service.impl.base_impl import BaseImpl, _result_handler
from main.service.utility.logger import log


class ProjectionImpl(BaseImpl):
    def __init__(self):
        super().__init__(ProjectionFacade)

    def create(self, data):
        try:
            log.info(str(data))
            movie_id = data['projection-movie']
            hall_id = data['projection-hall']
            date_from = data['projection-from']
            date_to = data['projection-to']
            time = data['projection-time']

            projection = Projection(movie_id=movie_id, hall_id=hall_id, date_from=date_from, date_to=date_to, time=time)

            return _result_handler(item=self.T.create(projection))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


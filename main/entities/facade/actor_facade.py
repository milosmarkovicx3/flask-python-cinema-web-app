from main.entities.facade.base_facade import BaseFacade
from main.entities.models.actor import Actor

class ActorFacade(BaseFacade):
    def __init__(self):
        super().__init__(Actor)



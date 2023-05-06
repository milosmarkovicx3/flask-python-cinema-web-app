from main.entities.dto.actor_role import ActorDTO
from main.entities.dto.genre_dto import GenreDTO
from main.entities.facade.base_facade import BaseFacade
from main.entities.models.movie import Movie


class MovieFacade(BaseFacade):
    def __init__(self):
        super().__init__(Movie)

    def find(self, value, column):
        response = super().find(value, column)
        if response:
            actors = []
            genres = []
            for ma in response.actors_association:
                actors.append(ActorDTO(id=ma.actor.id, name=ma.actor.name, image=ma.actor.image, role=ma.role))
            for mg in response.genres_association:
                genres.append(GenreDTO(id=mg.genre.id, name=mg.genre.name, image=mg.genre.image))
            return [response, actors, genres]

        return response





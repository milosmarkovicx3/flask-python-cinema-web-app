from flask_login import current_user
from main.entities.core.status import Status
from main.entities.facade.movie_facade import MovieFacade
from main.entities.facade.review_facade import ReviewFacade
from main.entities.core.result import Result, result_handler
from main.entities.models.review import Review
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log

mf = MovieFacade()

class ReviewImpl(BaseImpl):
    def __init__(self):
        super().__init__(ReviewFacade)

    def create(self, form):
        try:
            movie_id = form.get('movie_id')
            comment = form.get('comment')
            rating = form.get('rating')

            if not current_user.is_authenticated:
                return Result(status=Status.UNAUTHORIZED).response()

            if not mf.find(value=movie_id) or not rating or (comment and len(comment) >= 2048):
                return Result(status=Status.BAD_REQUEST).response()

            user_id = current_user.get_id()
            review = Review(
                movie_id=movie_id,
                user_id=user_id,
                comment=comment,
                rating=rating
            )
            return result_handler(item=self.T.create(review))
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()



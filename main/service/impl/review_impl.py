import traceback
from datetime import datetime
from flask_login import current_user
from main.entities.core.status import Status
from main.entities.facade.review_facade import ReviewFacade
from main.entities.core.result import Result, result_handler
from main.entities.models.review import Review
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log


class ReviewImpl(BaseImpl):
    def __init__(self):
        super().__init__(ReviewFacade)

    def create(self, data):
        try:


            movie_id = data['movie_id']
            comment = data['comment']
            rating = data['rating']
            created_at = datetime.now().date()

            if len(comment) >= 2048:
                result = Result(
                    status=Status.BAD_REQUEST,
                    description='Error: maksimalni broj karaktera za komentar je 2048.'
                )
                return result.response()
            if not current_user.is_authenticated:
                result = Result(
                    status=Status.UNAUTHORIZED,
                    description='Error: samo ulogovani korisnici mogu da ostave recenziju.'
                )
                return result.response()

            user_id = current_user.get_id()

            review = Review(movie_id=movie_id, user_id=user_id, comment=comment, rating=rating, created_at=created_at)

            return result_handler(item=self.T.create(review))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


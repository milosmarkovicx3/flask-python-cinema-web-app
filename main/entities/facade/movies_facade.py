from ..entities.movies import movies
from ..utility.logger import log

#
# def get_by_id(id):
#     try:
#         return movies.query.get(id)
#     except Exception as e:
#         log.error(e)
#         return str(e)
#
#
# def get_actors_by(id):
#     return movies.query.get(id).actors
#

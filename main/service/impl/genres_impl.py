from log.logger import log
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import genres_facade as gf

def get_by_id(id):
    try:
        result = Result(item = gf.get_by_id(id))
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

def get_all():
    try:
        result = Result(item = gf.get_all())
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'
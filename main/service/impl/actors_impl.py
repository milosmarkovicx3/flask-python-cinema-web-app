from log.logger import log
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import actors_facade as af

def get_by_id(id):
    try:
        result = Result(item = af.get_by_id(id))
        if result.get_item() is None:
            result.set_status(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

def get_all():
    try:
        result = Result(item = af.get_all())
        if result.get_item() is None:
            result.set_status(Result.INTERNAL_SERVER_ERROR)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'
from log.logger import log
from service.utility.utility import toJSON
from entities.core.result import Result
from entities.facade import movies_facade as mf

def get_by_id(id):
    try:
        result = Result(item = mf.get_by_id(id))
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'

def get_all():
    try:
        result = Result(item = mf.get_all())
        if result.get_item() is None:
            result.set_status(Result.NOT_FOUND)
        return toJSON(result)
    except Exception as e:
        log.error(e)
        return f'Dogodila se greška! [ {str(e)} ]'
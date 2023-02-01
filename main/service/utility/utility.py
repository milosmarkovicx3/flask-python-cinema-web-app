from flask import jsonify
from markupsafe import escape

def toJSON(entity_array):
    result = []
    for entity in entity_array:
        result.append(entity.__repr__())
    return escape(jsonify(result))


from flask import jsonify
from markupsafe import escape

def toJSON(entity):
    return jsonify(entity.__repr__())
    #return escape(jsonify(result))


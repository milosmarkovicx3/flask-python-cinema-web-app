from flask import jsonify
from markupsafe import escape


def json(entity):
    return jsonify(entity.__repr__())
    #return escape(jsonify(result))


from flask import Blueprint, request
from main.service.impl.genre_impl import GenreImpl

genre_api = Blueprint('genre_api', __name__, url_prefix='/genre')
gi = GenreImpl()

@genre_api.route('/<string:value>', methods=['GET'])
@genre_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return gi.find(value, column)

@genre_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return gi.find_all(kwargs)

@genre_api.route('/', methods=['POST'])
def create():
    return gi.create(request.form, request.files)

@genre_api.route('/', methods=['DELETE'])
def delete():
    return gi.delete(request.form)



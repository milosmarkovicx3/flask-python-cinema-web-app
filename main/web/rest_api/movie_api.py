from flask import Blueprint, request
from main.service.impl.movie_impl import MovieImpl

movie_api = Blueprint('movie_api', __name__, url_prefix='/movie')
mi = MovieImpl()


@movie_api.route('/<string:value>', methods=['GET'])
@movie_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return mi.find(value, column)


@movie_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return mi.find_all(kwargs)


@movie_api.route('/', methods=['POST'])
def create():
    return mi.create(request.form, request.files)


@movie_api.route('/', methods=['DELETE'])
def delete():
    return mi.delete(request.form)





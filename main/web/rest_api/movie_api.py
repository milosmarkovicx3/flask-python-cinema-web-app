from service.impl.movie_impl import MovieImpl
from flask import Blueprint, request

movie_api = Blueprint('movie_api', __name__)
mi = MovieImpl()


@movie_api.route('/<string:value>', methods=['GET'])
@movie_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column="id"):
    return mi.find(value, column)


@movie_api.route('/', methods=['GET'])
def find_all():
    kwargs = {}
    for key, value in request.args.items():
        kwargs[key] = value
    return mi.find_all(**kwargs)


@movie_api.route('/', methods=['POST'])
def create():
    return mi.create(data=request.form)


@movie_api.route('/<string:value>', methods=['DELETE'])
@movie_api.route('/<string:value>/<string:column>', methods=['DELETE'])
def delete(value, column="id"):
    return mi.delete(value, column)



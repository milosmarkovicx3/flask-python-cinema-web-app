from service.impl.movie_impl import MovieImpl
from flask import Blueprint, request

movie_api = Blueprint('movie_api', __name__)
mi = MovieImpl()
@movie_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return mi.get_by_id(id)

@movie_api.route('/<string:title>', methods=['GET'])
def get_by_title(title):
    return mi.get_by_title(title)

@movie_api.route('/', methods=['GET'])
def get_all():
    return mi.get_all()

@movie_api.route('/', methods=['POST'])
def create():
    return mi.create(request.form)

@movie_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return mi.delete_by_id(id)



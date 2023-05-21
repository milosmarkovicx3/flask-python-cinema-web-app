from flask import Blueprint, request
from main.service.impl.movie_impl import MovieImpl

movie_api = Blueprint('movie_api', __name__, url_prefix='/movie')
mi = MovieImpl()

@movie_api.route('/', methods=['GET'])
def find():
    return mi.find(**request.args)

@movie_api.route('/s', methods=['GET'])
def find_all():
    return mi.find_all(**request.args)

@movie_api.route('/', methods=['POST'])
def create():
    return mi.create(request.form, request.files)

@movie_api.route('/', methods=['DELETE'])
def delete():
    return mi.delete(**request.form)





from flask import Blueprint, request
from main.service.impl.genre_impl import GenreImpl

genre_api = Blueprint('genre_api', __name__, url_prefix='/genre')
gi = GenreImpl()

@genre_api.route('/', methods=['GET'])
def find():
    return gi.find(**request.args)

@genre_api.route('/s', methods=['GET'])
def find_all():
    return gi.find_all(**request.args)

@genre_api.route('/', methods=['POST'])
def create():
    return gi.create(request.form, request.files)

@genre_api.route('/', methods=['DELETE'])
def delete():
    return gi.delete(**request.form)



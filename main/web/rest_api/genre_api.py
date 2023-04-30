from service.impl.genre_impl import GenreImpl
from flask import Blueprint, request

genre_api = Blueprint('genre_api', __name__)
gi = GenreImpl()
@genre_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return gi.get_by_id(id)

@genre_api.route('/<string:name>', methods=['GET'])
def get_by_name(name):
    return gi.get_by_name(name)

@genre_api.route('/', methods=['GET'])
def get_all():
    return gi.get_all()

@genre_api.route('/', methods=['POST'])
def create():
    return gi.create(request.form)

@genre_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return gi.delete_by_id(id)



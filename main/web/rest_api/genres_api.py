from service.impl import genres_impl as gi
from flask import Blueprint, request

genres_api = Blueprint('genres_api', __name__)

@genres_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return gi.get_by_id(id)

@genres_api.route('/<string:name>', methods=['GET'])
def get_by_name(name):
    return gi.get_by_name(name)

@genres_api.route('/', methods=['GET'])
def get_all():
    return gi.get_all()

@genres_api.route('/', methods=['POST'])
def create():
    return gi.create(request.form)

@genres_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return gi.delete_by_id(id)



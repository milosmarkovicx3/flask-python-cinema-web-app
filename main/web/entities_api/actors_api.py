from service.impl import actors_impl as ai
from flask import Blueprint, request

actors_api = Blueprint('actors_api', __name__)

@actors_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return ai.get_by_id(id)

@actors_api.route('/<string:name>', methods=['GET'])
def get_by_name(name):
    return ai.get_by_name(name)

@actors_api.route('/', methods=['GET'])
def get_all():
    return ai.get_all()

@actors_api.route('/', methods=['POST'])
def create():
    return ai.create(request.form)

@actors_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return ai.delete_by_id(id)



from service.impl.actor_impl import ActorImpl
from flask import Blueprint, request

actor_api = Blueprint('actor_api', __name__)
ai = ActorImpl()

@actor_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return ai.get_by_id(id)

@actor_api.route('/<string:name>', methods=['GET'])
def get_by_name(name):
    return ai.get_by_name(name)

@actor_api.route('/', methods=['GET'])
def get_all():
    return ai.get_all()

@actor_api.route('/', methods=['POST'])
def create():
    return ai.create(request.form)

@actor_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return ai.delete_by_id(id)



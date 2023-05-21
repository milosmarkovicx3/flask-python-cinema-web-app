from flask import Blueprint, request
from main.service.impl.actor_impl import ActorImpl

actor_api = Blueprint('actor_api', __name__, url_prefix='/actor')
ai = ActorImpl()

@actor_api.route('/', methods=['GET'])
def find():
    return ai.find(**request.args)

@actor_api.route('/s', methods=['GET'])
def find_all():
    return ai.find_all(**request.args)

@actor_api.route('/', methods=['POST'])
def create():
    return ai.create(request.form, request.files)

@actor_api.route('/', methods=['DELETE'])
def delete():
    return ai.delete(**request.form)




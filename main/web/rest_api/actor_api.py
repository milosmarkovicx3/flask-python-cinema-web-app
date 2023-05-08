from flask import Blueprint, request
from main.service.impl.actor_impl import ActorImpl


actor_api = Blueprint('actor_api', __name__, url_prefix='/actor')
ai = ActorImpl()


@actor_api.route('/<string:value>', methods=['GET'])
@actor_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return ai.find(value, column)


@actor_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return ai.find_all(kwargs)

@actor_api.route('/', methods=['POST'])
def create():
    return ai.create(data=request.form, files=request.files)

@actor_api.route('/<string:value>', methods=['DELETE'])
@actor_api.route('/<string:value>/<string:column>', methods=['DELETE'])
def delete(value, column='id'):
    return ai.delete(value, column)



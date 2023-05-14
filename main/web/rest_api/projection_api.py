from flask import Blueprint, request
from main.service.impl.projection_impl import ProjectionImpl

projection_api = Blueprint('projection_api', __name__, url_prefix='/projection')
pi = ProjectionImpl()

@projection_api.route('/<string:value>', methods=['GET'])
@projection_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return pi.find(value, column)


@projection_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return pi.find_all(kwargs)

@projection_api.route('/', methods=['POST'])
def create():
    return pi.create(request.form)

@projection_api.route('/', methods=['DELETE'])
def delete():
    return pi.delete(request.form)




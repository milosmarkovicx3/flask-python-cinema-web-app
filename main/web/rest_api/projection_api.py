from flask import Blueprint, request
from main.service.impl.projection_impl import ProjectionImpl

projection_api = Blueprint('projection_api', __name__, url_prefix='/projection')
pi = ProjectionImpl()

@projection_api.route('/', methods=['GET'])
def find():
    return pi.find(**request.args)

@projection_api.route('/s', methods=['GET'])
def find_all():
    return pi.find_all(**request.args)

@projection_api.route('/', methods=['POST'])
def create():
    return pi.create(request.form)

@projection_api.route('/', methods=['DELETE'])
def delete():
    return pi.delete(**request.form)




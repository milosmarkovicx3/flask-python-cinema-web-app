from service.impl import movies_impl as mi
from flask import Blueprint, request

movies_api = Blueprint('movies_api', __name__)

@movies_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return mi.get_by_id(id)

@movies_api.route('/<string:title>', methods=['GET'])
def get_by_title(title):
    return mi.get_by_title(title)

@movies_api.route('/', methods=['GET'])
def get_all():
    return mi.get_all()

@movies_api.route('/', methods=['POST'])
def create():
    return mi.create(request.form)

@movies_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return mi.delete_by_id(id)



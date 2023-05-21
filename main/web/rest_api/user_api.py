from flask import Blueprint, request
from main.service.impl.user_impl import UserImpl

user_api = Blueprint('user_api', __name__, url_prefix='/user')
ui = UserImpl()

@user_api.route('/', methods=['GET'])
def find():
    return ui.find(**request.args)

@user_api.route('/s', methods=['GET'])
def find_all():
    return ui.find_all(**request.args)

@user_api.route('/', methods=['POST'])
def create():
    return ui.create(request.form)

@user_api.route('/', methods=['PUT'])
def update():
    return ui.update(request.form, request.files)

@user_api.route('/', methods=['DELETE'])
def delete():
    return ui.delete(**request.form)





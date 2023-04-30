from service.impl.user_impl import UserImpl
from flask import Blueprint, request

from service.utility.logger import log
from service.utility.utility import json

user_api = Blueprint('user_api', __name__)
ui = UserImpl()

@user_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return json(ui.find_by())
    # return ui.get_by_id(id)

@user_api.route('/', methods=['GET'])
def get_all():
    return ui.get_all()

@user_api.route('/', methods=['POST'])
def create():
    return ui.create(data=request.form)


@user_api.route('/<int:id>', methods=['DELETE'])
def delete_by_id(id):
    return ui.delete_by_id(id)



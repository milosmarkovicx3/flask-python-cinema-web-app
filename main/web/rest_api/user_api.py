import logging

from flask import Blueprint, request
from main.service.impl.user_impl import UserImpl
from main.service.utility.logger import log

user_api = Blueprint('user_api', __name__, url_prefix='/user')
ui = UserImpl()

@user_api.route('/<string:value>', methods=['GET'])
@user_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return ui.find(value, column)

@user_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return ui.find_all(kwargs)

@user_api.route('/', methods=['POST'])
def create():
    return ui.create(request.form)

@user_api.route('/', methods=['PUT'])
def update():
    return ui.update(request.form, request.files)

@user_api.route('/', methods=['DELETE'])
def delete():
    return ui.delete(request.form)





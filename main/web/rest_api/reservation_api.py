from flask import Blueprint, request
from main.service.impl.reservation_impl import ReservationImpl

reservation_api = Blueprint('reservation_api', __name__, url_prefix='/reservation')
ri = ReservationImpl()

@reservation_api.route('/', methods=['GET'])
def find():
    return ri.find(**request.args)

@reservation_api.route('/s', methods=['GET'])
def find_all():
    return ri.find_all(**request.args)

@reservation_api.route('/', methods=['POST'])
def create():
    return ri.create(request.form)

@reservation_api.route('/', methods=['DELETE'])
def delete():
    return ri.delete(**request.form)



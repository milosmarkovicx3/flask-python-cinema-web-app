from flask import Blueprint, request
from main.service.impl.reservation_impl import ReservationImpl

reservation_api = Blueprint('reservation_api', __name__, url_prefix='/reservation')
ri = ReservationImpl()

@reservation_api.route('/<string:value>', methods=['GET'])
@reservation_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return ri.find(value, column)


@reservation_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return ri.find_all(kwargs)

@reservation_api.route('/', methods=['POST'])
def create():
    return ri.create(request.form)

@reservation_api.route('/', methods=['DELETE'])
def delete():
    return ri.delete(request.form)



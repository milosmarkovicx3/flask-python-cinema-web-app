from flask import Blueprint, request
from main.service.impl.review_impl import ReviewImpl

review_api = Blueprint('review_api', __name__, url_prefix='/review')
ri = ReviewImpl()

@review_api.route('/<string:value>', methods=['GET'])
@review_api.route('/<string:value>/<string:column>', methods=['GET'])
def find(value, column='id'):
    return ri.find(value, column)


@review_api.route('/', methods=['GET'])
def find_all():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return ri.find_all(kwargs)

@review_api.route('/', methods=['POST'])
def create():
    return ri.create(data=request.form)

@review_api.route('/<string:value>', methods=['DELETE'])
@review_api.route('/<string:value>/<string:column>', methods=['DELETE'])
def delete(value, column='id'):
    return ri.delete(value, column)



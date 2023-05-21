from flask import Blueprint, request
from main.service.impl.review_impl import ReviewImpl

review_api = Blueprint('review_api', __name__, url_prefix='/review')
ri = ReviewImpl()

@review_api.route('/', methods=['GET'])
def find():
    return ri.find(**request.args)

@review_api.route('/s', methods=['GET'])
def find_all():
    return ri.find_all(**request.args)

@review_api.route('/', methods=['POST'])
def create():
    return ri.create(request.form)

@review_api.route('/', methods=['DELETE'])
def delete():
    return ri.delete(**request.form)




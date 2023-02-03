from service.impl import actors_impl as ai
from flask import Blueprint

actors_api = Blueprint('actors_api', __name__)

@actors_api.route('/<int:id>', methods=['GET'])
def get_by_id(id):
    return ai.get_by_id(id)

@actors_api.route('/', methods=['GET','POST'])
def get_all():
    return ai.get_all()


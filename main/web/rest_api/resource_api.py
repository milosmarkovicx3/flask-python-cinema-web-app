import os
from flask import Blueprint, send_file, abort
from flask_login import login_required
from config import STATIC_DIR_PATH
from main.entities.facade.user_facade import UserFacade
from main.service.impl.user_impl import UserImpl
from main.service.utility.utils import find_directory_path

resource_api = Blueprint('resource_api', __name__, url_prefix='/resource')
ui = UserImpl()
uf = UserFacade()

@resource_api.route('/<directory>/<name>')
def get_image(directory, name):
    directory_path = find_directory_path(STATIC_DIR_PATH, directory)
    if directory_path:
        image_path = os.path.join(directory_path, name)
        if os.path.isfile(image_path):
            if name.endswith('.png'):
                return send_file(image_path, mimetype='image/png')
            else:
                return send_file(image_path, mimetype='image/jpg')
    abort(404)


@resource_api.route('/<value>', methods=['GET'])
@login_required
def download_user_data(value):
    return ui.generate_user_data(value, 'id')

import os
from flask import Blueprint, send_file, abort
from config import STATIC_DIR_PATH

resource_api = Blueprint('resource_api', __name__, url_prefix='/resource')

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


def find_directory_path(root_directory, directory_name):
    for root, dirs, files in os.walk(root_directory):
        if directory_name in dirs:
            return os.path.join(root, directory_name)
    return None
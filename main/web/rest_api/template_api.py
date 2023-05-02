import os
from flask import render_template, Blueprint, send_file
from flask_login import login_required
from service.core.wtf_forms import wtf_create_movie, wtf_create_actor, wtf_create_genre
from service.utility.logger import project_path


template_api = Blueprint('template_api', __name__)

@template_api.route('/EditDatabase', methods=['GET'])
@login_required
def dashboard():
    return render_template('EditDatabase.html', form_movie=wtf_create_movie(), form_actor=wtf_create_actor(), form_genre=wtf_create_genre())

@template_api.route('/logo')
def get_image():
    image_path = os.path.join(project_path, 'static\\resources\\images', 'arhiva_logo.jpg')
    return send_file(image_path, mimetype='image/jpg')
@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')
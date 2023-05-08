import logging

from flask import render_template, Blueprint, request, abort
from main.entities.facade.movie_facade import MovieFacade
from main.service.impl.movie_impl import MovieImpl
from main.web.rest_api.auth_api import admin_required

template_api = Blueprint('template_api', __name__, url_prefix='/')
mi = MovieImpl()
mf = MovieFacade()

@template_api.route('/admin-panel', methods=['GET'])
@admin_required
def dashboard():
    return render_template('dashboard.html')

@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@template_api.route('/film/<int:id>', methods=['GET'])
def movie(id):
    movie = mf.find(id, 'id').__repr__()
    return render_template('movie.html', movie=movie) if movie else abort(404)


@template_api.route('/repertoar', methods=['GET'])
def repertoire_search():
    kwargs = {k: v for k, v in request.args.items() if v is not None}
    paginate_object = mi.repertoire_search(kwargs)
    return render_template("repertoire.html",
                           pagination=paginate_object,
                           endpoint='template_api.repertoire_search',
                           form=kwargs)

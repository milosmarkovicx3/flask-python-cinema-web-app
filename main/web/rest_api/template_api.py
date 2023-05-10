from flask import render_template, Blueprint, request, abort
from main.entities.facade.hall_facade import HallFacade
from main.entities.facade.movie_facade import MovieFacade
from main.entities.facade.projection_facade import ProjectionFacade
from main.service.impl.movie_impl import MovieImpl
from main.web.rest_api.auth_api import admin_required

template_api = Blueprint('template_api', __name__, url_prefix='/')
mi = MovieImpl()
mf = MovieFacade()
hf = HallFacade()
pf = ProjectionFacade()

@template_api.route('/admin-panel', methods=['GET'])
@admin_required
def dashboard():
    movies = mf.find_all()
    halls = hf.find_all()
    return render_template('dashboard.html', movies=movies, halls=halls)

@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@template_api.route('/film/<int:id>', methods=['GET'])
def movie(id):
    entity = mf.find(id, 'id').__repr__()
    return render_template('movie.html', movie=entity) if entity else abort(404)

@template_api.route('/projekcija/<int:id>', methods=['GET'])
def projection(id):
    entity = pf.find(id, 'id').__repr__()
    return render_template('projection.html', projection=entity) if entity else abort(404)


@template_api.route('/repertoar', methods=['GET'])
def repertoire_search():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    paginate_object = mi.repertoire_search(**kwargs)
    return render_template("repertoire.html",
                           pagination=paginate_object,
                           endpoint='template_api.repertoire_search',
                           form=kwargs)

@template_api.app_template_filter('vote_count')
def format_vote_count(vote_count):
    """
    Jinja2 filter za formatiranje prikaza glasova.
    Globalna sintaksa bi bila '@app.template_filter'.
    Upotreba '{{ movie.votes | vote_count }}'.
    """
    return ''

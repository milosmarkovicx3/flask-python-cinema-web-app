from flask import render_template, Blueprint, request, abort
from flask_login import login_required, current_user
from main.entities.facade.hall_facade import HallFacade
from main.entities.facade.movie_facade import MovieFacade
from main.entities.facade.projection_facade import ProjectionFacade
from main.entities.facade.reservation_facade import ReservationFacade
from main.service.impl.movie_impl import MovieImpl
from main.service.utility import jinja2_filters
from main.service.utility.logger import log
from main.service.utility.utils import repr_helper_method
from main.web.rest_api.auth_api import admin_required

template_api = Blueprint('template_api', __name__, url_prefix='/')
mi = MovieImpl()
mf = MovieFacade()
hf = HallFacade()
pf = ProjectionFacade()
rf = ReservationFacade()


@template_api.route('/admin-panel', methods=['GET'])
@admin_required
def dashboard():
    movies = mf.find_all()
    halls = hf.find_all()
    return render_template('dashboard.html', movies=movies, halls=halls)


@template_api.route('/rezervacije', methods=['GET'])
@login_required
def reservations():
    entities = rf.find_all(column='user_id', value=current_user.id)
    if entities:
        return render_template('reservations.html', reservations=repr_helper_method(entities))
    return render_template('reservations.html')


@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@template_api.route('/film/<int:id>', methods=['GET'])
def movie(id):
    entity = mf.find(id, 'id').__repr__()
    return render_template('movie.html', movie=entity) if entity else abort(404)


@template_api.route('/projekcija/<int:projection_id>/<string:date>', methods=['GET'])
def projection(projection_id, date):
    entity = pf.find(projection_id, 'id').__repr__()
    return render_template('projection.html', projection=entity, date=date) if entity else abort(404)


@template_api.route('/repertoar', methods=['GET'])
def repertoire_search():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    paginate_object = mi.repertoire_search(**kwargs)
    return render_template("repertoire.html",
                           pagination=paginate_object,
                           endpoint='template_api.repertoire_search',
                           form=kwargs)


@template_api.app_template_filter('enumerate')
def enumerate_filter(iterable):
    """
    Jinja2 filter za lakše prolaženje proz petlju.
    Globalna sintaksa bi bila '@app.template_filter'.
    """
    return enumerate(iterable)


@template_api.app_template_filter('format_date')
def get_formated_date_name(date):
    return jinja2_filters.get_formated_date_name_filter(date)

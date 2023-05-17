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

# -OPCIJE-PROFILA-------------------------------------------------------------------------------------------------------

@template_api.route('/admin-panel', methods=['GET'])
@admin_required
def dashboard():
    movies = mf.find_all()
    halls = hf.find_all()
    return render_template('profile/dashboard.html', movies=movies, halls=halls)

@template_api.route('/profil', methods=['GET'])
@login_required
def profile():
    return render_template('profile/profile.html')

@template_api.route('/rezervacije', methods=['GET'])
@login_required
def reservations():
    entities = rf.find_all(column='user_id', value=current_user.id)
    return render_template('profile/reservations.html', reservations=repr_helper_method(entities))

@template_api.route('/podešavanja', methods=['GET'])
@login_required
def settings():
    return render_template('profile/settings.html')

@template_api.route('/zaboravljena-lozinka', methods=['GET'])
def forgotten_password():
    return render_template('profile/forgotten_password.html')

@template_api.route('/nova-lozinka', methods=['GET'])
def new_password():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    return render_template('profile/new_password.html', **kwargs)
# ----------------------------------------------------------------------------------------------------------------------

# -GLAVNA-NAVIGACIJA----------------------------------------------------------------------------------------------------

@template_api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@template_api.route('/repertoar', methods=['GET'])
def repertoire():
    kwargs = {k: v for k, v in request.args.items() if v is not (None or '')}
    paginate = mi.repertoire(**kwargs)
    if 'page' in kwargs: del kwargs['page']
    return render_template("repertoire.html", pagination=paginate, endpoint='template_api.repertoire', form=kwargs)

@template_api.route('/članstvo', methods=['GET'])
def membership():
    return render_template('membership.html')

@template_api.route('/događaji', methods=['GET'])
def events():
    return render_template('events.html')

@template_api.route('/kontakt', methods=['GET'])
def contact():
    return render_template('contact.html')
# ----------------------------------------------------------------------------------------------------------------------

# -FILM-GRUPA-----------------------------------------------------------------------------------------------------------

@template_api.route('/film/<int:id>', methods=['GET'])
def movie(id):
    entity = mf.find(id, 'id').__repr__()
    return render_template('movie.html', movie=entity) if entity else abort(404)

@template_api.route('/projekcija/<int:projection_id>/<string:date>', methods=['GET'])
def projection(projection_id, date):
    entity = pf.find(projection_id, 'id').__repr__()
    return render_template('projection.html', projection=entity, date=date) if entity else abort(404)
# ----------------------------------------------------------------------------------------------------------------------

# -DOGAĐAJI-------------------------------------------------------------------------------------------------------------

@template_api.route('/online-kupovina', methods=['GET'])
def online_shopping():
    return render_template('events/online_shopping.html')

@template_api.route('/proslavi-rođendan-kao-na-filmu', methods=['GET'])
def arhiv_party():
    return render_template('events/arhiv_party.html')

@template_api.route('/arhiv-bonus-kartica', methods=['GET'])
def bonus_card():
    return render_template('events/bonus_card.html')

@template_api.route('/specilajni-meni', methods=['GET'])
def arhiv_meal():
    return render_template('events/arhiv_meal.html')

@template_api.route('/arhiv-porodica', methods=['GET'])
def arhiv_family():
    return render_template('events/arhiv_family.html')

@template_api.route('/besplatne-kokice', methods=['GET'])
def arhiv_popcorns():
    return render_template('events/arhiv_popcorns.html')

@template_api.route('/arhiv-utorak', methods=['GET'])
def arhiv_tuesday():
    return render_template('events/arhiv_tuesday.html')
# ----------------------------------------------------------------------------------------------------------------------

# -FOOTER---------------------------------------------------------------------------------------------------------------

@template_api.route('/često-postavljana-pitanja', methods=['GET'])
def faq():
    return render_template('footer/faq.html')

@template_api.route('/politika-privatnosti', methods=['GET'])
def privacy_politics():
    return render_template('footer/privacy_politics.html')

@template_api.route('/uslovi-poslovanja', methods=['GET'])
def terms_and_conditions():
    return render_template('footer/terms_and_conditions.html')

@template_api.route('/o-nama', methods=['GET'])
def about_us():
    return render_template('footer/about_us.html')
# ----------------------------------------------------------------------------------------------------------------------

# -JINJA2-FILTERI-------------------------------------------------------------------------------------------------------

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
# ----------------------------------------------------------------------------------------------------------------------
import inspect
from functools import wraps
from flask import request, Blueprint, session, abort
from flask_login import login_required, LoginManager, current_user
from main.entities.models.user import User
from main.service.impl.user_impl import UserImpl

auth_api = Blueprint('auth_api', __name__, url_prefix='/')
login_manager = LoginManager()
ui = UserImpl()

@auth_api.route('/login', methods=['POST'])
def login():
    return ui.login(request.form)

@auth_api.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    return ui.logout()

@auth_api.route('/confirm-email', methods=['GET'])
def confirm_email():
    kwargs = {k: v for k, v in request.args.items() if v and k in inspect.signature(ui.confirm_email).parameters}
    return ui.confirm_email(**kwargs)

@auth_api.route('/forgotten-password', methods=['POST'])
def forgotten_password():
    return ui.forgotten_password(request.form)

@login_manager.user_loader
def load_user(user_id):
    """
    Ugrađena metoda flask-login plugina za učitavanje korisnika.
    """
    return User.query.get(int(user_id))

def admin_required(func):
    """
    Custom dekorator funkcija za praćenje permisija.
    """
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_superuser:
            return abort(401)
        return func(*args, **kwargs)
    return decorated_view

@login_required
def check_auth_token():
    """
    Unutar 'flask_app.py' fajla deklarisan poziv ove funkcije pre
    svakog poziva korisnika. Deklaracija mora da se nalazi u samom
    root fajlu aplicije, jer inače dolazi do rekurzivnog importa
    usled app promenljive u '@app.before_request'. Funkcija sama
    po sebi izloguje već ulogovane korisnike, ako se neko u među-
    vremenu prijavio sa njihovim nalogom na drugog uređaju.
    """
    if current_user.is_authenticated and session.get('auth_token') != current_user.auth_token:
        ui.logout()

@login_required
def ping():
    """
    Identična situacija kao za 'check_auth_token' funkciju iznad.
    Prati se poslednja aktivnost korisnika na sajtu.
    """
    if current_user.is_authenticated:
        current_user.ping()

@auth_api.context_processor
def inject_data():
    """
    Кoristi se da se pošalju podaci iz sesije koji su setovani u
    xzy metodi i ujedno izbrišu iz same. Predviđen slučaj korišćena,
    koristik je poslao zahtev za registraciju, ali podaci iz forme
    nisu prošli validaciju, pa se sami vraćaju da korisnik ne bi
    morao da unosi sve podatke ponovo.
    """
    form_data = session.pop('form_data', None)
    return {'form_data': form_data}
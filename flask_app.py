import os
from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import current_user
from main.entities.core.base import db
from main.service.core.bcrypt import bcrypt
from main.service.core.wtf_forms import csrf
from main.service.utility.mail import mail
from main.web.rest_api.auth_api import login_manager, auth_api, check_auth_token, ping
from main.web.rest_api.projection_api import projection_api
from main.web.rest_api.reservation_api import reservation_api
from main.web.rest_api.resource_api import resource_api
from main.web.rest_api.review_api import review_api
from main.web.rest_api.template_api import template_api
from main.web.rest_api.genre_api import genre_api
from main.web.rest_api.actor_api import actor_api
from main.web.rest_api.movie_api import movie_api
from main.web.rest_api.user_api import user_api

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["WTF_CSRF_SECRET_KEY"] = os.environ.get("WTF_CSRF_SECRET_KEY")
app.config["SECURITY_PASSWORD_SALT"] = os.environ.get("SECURITY_PASSWORD_SALT")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URI", "mysql://root:@localhost/arhiv")
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 280}
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.getenv("MAIL_DEFAULT_SENDER")
app.config["MAIL_USE_SSL"] = os.getenv("MAIL_USE_SSL")
app.config["MAIL_USE_TLS"] = os.getenv("MAIL_USE_TLS")
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
"""
Ograničava kolačiće da se koriste samo na HTTPS standardu prometa podataka.
"""
app.config['SESSION_COOKIE_SECURE'] = True
"""
Sprečava mogućnost čitanja sadržaja kolačića preko JavaScript-a.
"""
app.config['SESSION_COOKIE_HTTPONLY'] = True
"""
Flask aplikacija u scenariju gde je recimo ona middle-man za neki API, sprečava
slanje kolačića koje je primila od strane klijentovog pretraživača sa zahtevima
ka eksternih sajtova koji su skloni CSRF napadima.
"""
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
"""
Na pythonanywhere hostingu mora da se isključi inače se dobija csrf token
missing/missmatching flag, inače ovakav problem je usko povezan isto kada je
cookie_secure flag stavljen na true, a sajt pritom ne koristi https standard.
"""
app.config['SESSION_COOKIE_DOMAIN'] = False
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(actor_api)
app.register_blueprint(genre_api)
app.register_blueprint(movie_api)
app.register_blueprint(user_api)
app.register_blueprint(template_api)
app.register_blueprint(auth_api)
app.register_blueprint(resource_api)
app.register_blueprint(projection_api)
app.register_blueprint(review_api)
app.register_blueprint(reservation_api)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    if current_user.is_authenticated:
        check_auth_token()
        ping()

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    response.headers["Cache-Control"] = "public, max-age=60, must-revalidate"
    return response


login_manager.init_app(app)
login_manager.login_view = "template_api.index"
mail.init_app(app)
csrf.init_app(app)
db.init_app(app)
bcrypt.init_app(app)

# -ISKLJUČITI-NA-PRODUKCIJI-----------------------------------------------------
# app.app_context().push()
# db.create_all()
# ------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)




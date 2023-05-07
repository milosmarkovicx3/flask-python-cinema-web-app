# https://flask.palletsprojects.com/en/2.3.x/security/#security-csp
import os
from flask import Flask, render_template
from dotenv import load_dotenv
from main.entities.core.base import db
from main.entities.facade.hall_facade import HallFacade
from main.entities.facade.seat_facade import SeatFacade
from main.entities.facade.seat_type_facade import SeatTypeFacade
from main.entities.models.seat import Seat
from main.service.core.wtf_forms import csrf
from main.service.impl.seat_impl import SeatImpl
from main.service.utility.mail import mail
from main.web.rest_api.auth_api import login_manager, auth_api
from main.web.rest_api.resource_api import resource_api
from main.web.rest_api.template_api import template_api
from main.web.rest_api.genre_api import genre_api
from main.web.rest_api.actor_api import actor_api
from main.web.rest_api.movie_api import movie_api
from main.web.rest_api.user_api import user_api

app = Flask(__name__)

load_dotenv()

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["WTF_CSRF_SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SECURITY_PASSWORD_SALT"] = os.environ.get("SECURITY_PASSWORD_SALT")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "mysql://root:@localhost/arhiv")
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = "office@arhiv.com"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TLS"] = False
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(actor_api)
app.register_blueprint(genre_api)
app.register_blueprint(movie_api)
app.register_blueprint(user_api)
app.register_blueprint(template_api)
app.register_blueprint(auth_api)
app.register_blueprint(resource_api)


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


login_manager.init_app(app)
login_manager.login_view = "template_api.index"
mail.init_app(app)
csrf.init_app(app)
db.init_app(app)
app.app_context().push()
db.create_all()






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # produkcija debug=False


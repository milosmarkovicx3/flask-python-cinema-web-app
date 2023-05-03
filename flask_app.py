# https://flask.palletsprojects.com/en/2.3.x/security/#security-csp
import os
from flask import Flask
from dotenv import load_dotenv
from entities.core.base import db
from service.core.wtf_forms import csrf
from service.utility.mail import mail
from web.rest_api.auth_api import login_manager, auth_api
from web.rest_api.template_api import template_api
from web.rest_api.genre_api import genre_api
from web.rest_api.actor_api import actor_api
from web.rest_api.movie_api import movie_api
from web.rest_api.user_api import user_api

app = Flask(__name__)
# template_folder=f'{project_path}templates',
# static_folder=f'{project_path}static'

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
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(actor_api, url_prefix='/actor')
app.register_blueprint(genre_api, url_prefix='/genre')
app.register_blueprint(movie_api, url_prefix='/movie')
app.register_blueprint(user_api, url_prefix='/user')
app.register_blueprint(template_api, url_prefix='/')
app.register_blueprint(auth_api, url_prefix='/')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    return response




login_manager.init_app(app)
login_manager.login_view = "template_api.index"
mail.init_app(app)
csrf.init_app(app)
db.init_app(app)
app.app_context().push()
db.create_all()


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)  # produkcija debug=False



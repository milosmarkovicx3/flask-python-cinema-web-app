import os
from flask import Flask, Blueprint
from dotenv import load_dotenv
from flask_login import LoginManager
from flask_mail import Mail, Message
from flask_wtf import CSRFProtect

from entities.core.base import db
from entities.models.user import User
from service.utility.logger import project_path
from service.utility.mail import mail
from web.rest_api.auth_api import login_manager, auth_api
from web.rest_api.template_api import template_api
from web.rest_api.genre_api import genre_api
from web.rest_api.actor_api import actor_api
from web.rest_api.movie_api import movie_api
from web.rest_api.user_api import user_api

load_dotenv()

app = Flask(
    __name__,
    template_folder=f'{project_path}templates',
    static_folder=f'{project_path}static'
)


app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "0aedgaii451cef0af8bd6432ec4b317")
# secrets.token_urlsafe()
app.config["WTF_CSRF_SECRET_KEY"] = os.environ.get("SECRET_KEY", "0aedgaii451cef0af8a6432ec4b317c")
# u slučaju da nije konfigurisan koristi se secret_key kao zamena
app.config["SECURITY_PASSWORD_SALT"] = os.environ.get("SECURITY_PASSWORD_SALT", "ab3d3a0f6984c4f5hkao41509b0")
# bcrypt plugin je default za SECURITY_PASSWORD_HASH, koji zahteva slani ključ
# secrets.SystemRandom().getrandbits(128)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "mysql://root:@localhost/cinema")
app.config["MAIL_SERVER"] = os.getenv("MAIL_SERVER")
app.config["MAIL_PORT"] = os.getenv("MAIL_PORT")
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")
# #https://myaccount.google.com/apppasswords
app.config["MAIL_DEFAULT_SENDER"] = "office@arhiv.com"
app.config["MAIL_USE_SSL"] = True  # je najčešće za port 465?
app.config["MAIL_USE_TLS"] = False # je najčešće za port 587?
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
mail.init_app(app)



login_manager.login_view = "auth_api.login"

csrf = CSRFProtect(app)

db.init_app(app)
app.app_context().push()
db.create_all()

    #show_all()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
    # za produkciju skinuti debug


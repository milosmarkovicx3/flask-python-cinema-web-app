import os
from flask import Flask, render_template, flash
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from flask_mail import Mail, Message
from flask_login import LoginManager

from service.utility.logger import project_path
from entities.core.base import db
from entities.models.user import User
from service.core.wtf_forms import *
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
app.config["MAIL_DEFAULT_SENDER"] = "office@arhiv.com"
app.config["MAIL_USE_SSL"] = True  # je najčešće za port 465?
app.config["MAIL_USE_TLS"] = False # je najčešće za port 587?
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'
app.config['JSON_AS_ASCII'] = False

# ostavljam čisto radi reda ako se nekad odlučim da plaćam mesečnu pretplatu ili uzmem novi trial
# app.config['RECAPTCHA_USE_SSL'] = False
# app.config['RECAPTCHA_PUBLIC_KEY'] = '6LcMkHshAAAAAOsgybf6CkOi9R0vXugojWzTMqTl'
# app.config['RECAPTCHA_PRIVATE_KEY'] = '6LcMkHshAAAAACIX71ZTnSDZ-6XuobY8i0micU5W'
# app.config['RECAPTCHA_OPTIONS'] = {'theme': 'dark'}


# -------------------------------------------------------
login_manager = LoginManager()
login_manager.init_app(app)
mail = Mail(app)
csrf = CSRFProtect(app)
# {{ form.csrf_token }}


@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    return response

app.register_blueprint(actor_api, url_prefix='/actor')
app.register_blueprint(genre_api, url_prefix='/genre')
app.register_blueprint(movie_api, url_prefix='/movie')
app.register_blueprint(user_api, url_prefix='/user')

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
# -------------------------------------------------------
#
#
# @app.errorhandler(413)
# def fileSizeError(e):
#     print("[error: 413] Veličina datoteke prelazi dozvoljenu granicu!")



# #---------------------------------------------------------------------------------------------------

#
# def registerUser(req):
#     first_name = req.form['first-name']
#     last_name = req.form['last-name']
#     email = req.form['email']
#     password = req.form['password']
#

@app.route('/EditDatabase', methods=['GET'])
def EditDatabase():
    return render_template('EditDatabase.html', form_movie=wtf_create_movie(), form_actor=wtf_create_actor(), form_genre=wtf_create_genre())

@app.route('/', methods=['GET'])
def index():
    rform = wtf_register()
    #lform =
    return render_template('index.html', rform=rform)
# @app.route('/register', methods=['POST'])
# def register():
#     flash('All fields are required.')
#     rform = wtf_register()
#     return ""

@app.route("/sendMailTest")
def sendMailTest():
    msg = Message('Hello', sender = 'vukman@gmail.com', recipients =['milos.dj.markovic@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    with app.open_resource("Capture1.JPG") as fp:
        msg.attach("Capture1.JPG", "image/jpg", fp.read())
    mail.send(msg)
    return "Sent"


''' from werkzeug.utils import secure_filename

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/path/to/save/' + secure_filename(f.filename))
 '''
 
'''  foo = request.cookies.get$('key') '''

''' foo = make_response(expression)
foo.set_cookie('key', 'value')
return foo '''




db.init_app(app)
app.app_context().push()
db.create_all()

    #show_all()
if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
    # za produkciju skinuti debug

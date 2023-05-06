from functools import wraps

from flask import request, Blueprint, session, abort
from flask_login import login_required, LoginManager, current_user
from main.entities.models.user import User
from main.service.impl.user_impl import UserImpl

auth_api = Blueprint('auth_api', __name__, url_prefix='/')
login_manager = LoginManager()
ui = UserImpl()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def admin_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_superuser:
            return abort(401)
        return func(*args, **kwargs)
    return decorated_view

@auth_api.route('/login', methods=['POST'])
def login():
    return ui.login(data=request.form)

@auth_api.context_processor
def inject_data():
    form_data = session.pop('form_data', None)
    return {'form_data': form_data}

@auth_api.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    return ui.logout()

@auth_api.route('/auth/<string:email>/<string:username_hash>', methods=['GET'])
def confirm_email(email, username_hash):
    return ui.confirm_email(email, username_hash)




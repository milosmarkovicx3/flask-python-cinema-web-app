import traceback
from datetime import datetime
from flask import make_response, redirect, request, url_for, session, flash
from flask_login import login_user, current_user, logout_user
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from entities.core.base import db
from entities.facade.user_facade import UserFacade
from entities.models.user import User
from service.impl.base_impl import BaseImpl
from service.utility.logger import log
from service.utility.mail import send_mail_confirm_email
from service.utility.utils import basic_regex, email_regex, passwd_regex


class UserImpl(BaseImpl):
    def __init__(self):
        super().__init__(UserFacade)

    def create(self, data):
        try:
            username = data['register-username']
            email = data['register-email']
            passwd = data['register-passwd']
            first_name = data['register-first-name']
            last_name = data['register-last-name']
            conditions = data.get('register-conditions')

            find_username = self.T.find(username, "username")
            find_email = self.T.find(email, "email")

            if (not basic_regex(username) or
                    not email_regex(email) or
                    not passwd_regex(passwd) or
                    not basic_regex(first_name) or
                    not basic_regex(last_name) or
                    not conditions or
                    find_username or
                    find_email):

                flash('register_fail', 'error')
                return redirect(request.referrer or url_for('template_api.index'))

            passwd_hash = pbkdf2_sha256.hash(passwd)

            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=passwd_hash,
                date_joined=datetime.now(),
                last_login_at=datetime.now(),
                login_count=1
            )

            if self.T.create(user):
                send_mail_confirm_email(msg_to=user.email, token=pbkdf2_sha256.hash(user.username))
                return redirect(request.referrer or url_for('template_api.index'))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return redirect(request.referrer or url_for('template_api.index'))

    def login(self, data):
        try:
            username = data["login-username"]
            password = data["login-passwd"]
            remember = data.get('login-conditions')

            log.info(f'login: {username}')
            user = self.T.find(username, "username")

            if user and pbkdf2_sha256.verify(secret=password, hash=user.password):
                login_user(user)

                user.last_login_at = datetime.now()
                user.login_count += 1
                user.last_login_ip = request.remote_addr
                db.session.commit()

                if remember:
                    response = make_response(redirect(request.referrer or url_for('template_api.index')))
                    response.set_cookie('archive', 'true', max_age=604800)  # 7 dana
                    return response
                return redirect(request.referrer or url_for('template_api.index'))

            else:
                flash('login_fail', 'error')
                session['form_data'] = data
                return redirect(request.referrer or url_for('template_api.index'))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return redirect(request.referrer or url_for('template_api.index'))

    def logout(self):
        try:
            log.info(f'log out: {current_user.first_name} {current_user.last_name}')
            logout_user()
            if request.cookies.get('archive'):
                response = make_response(redirect(request.referrer or url_for('template_api.index')))
                response.delete_cookie('archive')
                return response

            return redirect(request.referrer or url_for('template_api.index'))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return redirect(request.referrer or url_for('template_api.index'))

    def confirm_email(self, email, username_hash):
        try:
            user = self.T.find(email, "email")
            if user and pbkdf2_sha256.verify(secret=user.username, hash=username_hash):
                user.confirmed_at = datetime.now()
                db.session.commit()
            return '''
                    <html>
                        <body>
                            <script>
                                alert('Vaša email adresa je uspešno verifikovana!');
                            </script>
                        </body>
                    </html>
                    '''
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return redirect(request.referrer or url_for('template_api.index'))



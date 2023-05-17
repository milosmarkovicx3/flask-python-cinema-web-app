import base64
import os
import traceback
from datetime import datetime, timedelta
from json import dumps

from flask import make_response, redirect, request, url_for, session, flash, Response
from flask_login import login_user, current_user, logout_user
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from werkzeug.utils import secure_filename
from config import STATIC_DIR_PATH
from main.entities.core.base import db
from main.entities.core.result import Result, result_handler
from main.entities.core.status import Status
from main.entities.facade.user_facade import UserFacade
from main.entities.models.user import User
from main.service.core.wtf_forms import allowed_file
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log
from main.service.utility.mail import send_mail_confirm_email
from main.service.utility.utils import basic_regex, email_regex, passwd_regex


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

                result = Result(
                    status=Status.BAD_REQUEST,
                    description="Error: loš zahtev, poslate pogrešne vrednosti."
                )
                return result.response()

            passwd_hash = pbkdf2_sha256.hash(passwd)

            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=passwd_hash,
                date_joined=datetime.now(),
                login_count=0
            )

            if self.T.create(user):
                send_mail_confirm_email(username=username, msg_to=user.email, token=pbkdf2_sha256.hash(user.username))
                return result_handler(item=user)
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()


    def update(self, data, files):
        new_filename = ''
        try:
            username = data['profile-username']
            email = data['profile-email']
            passwd = data['profile-passwd']
            passwd_new = data['profile-passwd-new']
            first_name = data['profile-first-name']
            last_name = data['profile-last-name']
            date_of_birth = data['profile-date-of-birth']
            phone_number = data['profile-phone-number']
            image = files['profile-image']

            if not pbkdf2_sha256.verify(secret=passwd, hash=current_user.password):
                result = Result(
                    status=Status.BAD_REQUEST,
                    description="Error: pogrešna lozinka."
                )
                return result.response()

            find_username, find_email = False, False
            if current_user.username != username:
                find_username = self.T.find(value=username, column="username")
            if current_user.email != email:
                find_email = self.T.find_all(value=email, column="email")

            if (not basic_regex(username) or
                    not email_regex(email) or
                    not passwd_regex(passwd) or
                    not basic_regex(first_name) or
                    not basic_regex(last_name) or
                    find_username or
                    find_email):

                result = Result(
                    status=Status.BAD_REQUEST,
                    description="Error: loš zahtev, poslate pogrešne vrednosti."
                )
                return result.response()

            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                basename, extension = os.path.splitext(filename)
                new_filename = f"{current_user.id}{extension}"
                image.save(os.path.join(f'{STATIC_DIR_PATH}\\resources\\user-images\\', new_filename))
                current_user.image = new_filename

            if passwd_new:
                passwd_hash = pbkdf2_sha256.hash(passwd_new)
                current_user.password = passwd_hash

            current_user.username = username
            current_user.email = email
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.date_of_birth = date_of_birth
            current_user.phone_number = phone_number

            db.session.commit()

            return result_handler(item=True)
        except Exception as e:
            os.remove(os.path.join(f'{STATIC_DIR_PATH}\\resources\\user-images\\', new_filename))
            db.session.rollback()
            log.error(f"{e}\n{traceback.format_exc()}")
            result = Result(status=Status.INTERNAL_SERVER_ERROR)
            return result.response()

    def login(self, data):
        try:
            username = data["login-username"]
            password = data["login-passwd"]
            remember = data.get('login-conditions')

            log.info(f'login: {username}')
            user = self.T.find(username, "username")

            if user and pbkdf2_sha256.verify(secret=password, hash=user.password):
                login_user(user)

                login_user(user, remember=True, duration=timedelta(days=365)) if remember else login_user(user)

                user.last_login_at = datetime.now()
                user.login_count += 1
                user.last_login_ip = request.remote_addr
                """    
                Koristi se u svrhe izlogovanja korisnika kada se prijavi sa različitog uređaja.
                Postoji funkcija 'check_auth_token' koja se poziva pre svakog eksternog poziva
                korisnika sa uslovom da je prethodno ulogovan, gde se zatim proverava vrednost 
                'device_auth_token' kolone u bazi i u slučaju da se vrednosti razlikuju sistem
                će izlogovati korisnika.                
                """
                auth_token = user.generate_auth_token()
                user.auth_token = auth_token
                db.session.commit()
                session['auth_token'] = auth_token

                return redirect(request.referrer or url_for('template_api.index'))
            else:
                flash('login_fail', 'error')
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

    def confirm_email(self, email, token):
        try:
            user = self.T.find(email, "email")
            if user and pbkdf2_sha256.verify(secret=user.username, hash=token):
                user.confirmed_at = datetime.now()
                db.session.commit()
                flash('email_confirmed')
            return redirect(url_for('template_api.index'))
        except Exception as e:
            log.error(f"{e}\n{traceback.format_exc()}")
            return redirect(url_for('template_api.index'))

    def generate_user_data(self, value, column):
        user = self.T.find(value=value, column=column)
        if not user:
            return result_handler(item=False)
        data = user.__repr__()
        image_path = f'{STATIC_DIR_PATH}\\resources\\user-images\\{user.image}'
        with open(image_path, "rb") as img_file:
            image = str(base64.b64encode(img_file.read()))
        data['image_base64'] = image
        json_data = dumps(data, sort_keys=False, indent=4, ensure_ascii=False)
        response = Response(json_data, content_type='application/json')
        response.headers.set('Content-Disposition', 'attachment', filename='user_data.json')
        return response



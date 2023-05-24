import base64
import os
from datetime import datetime, timedelta
from json import dumps
from flask import make_response, redirect, request, url_for, session, flash, Response
from flask_login import login_user, current_user, logout_user
from werkzeug.utils import secure_filename
from config import STATIC_DIR_PATH
from main.entities.core.base import db
from main.entities.core.result import Result, result_handler
from main.entities.core.status import Status
from main.entities.facade.user_facade import UserFacade
from main.entities.models.user import User
from main.service.core.bcrypt import bcrypt
from main.service.core.wtf_forms import allowed_file
from main.service.impl.base_impl import BaseImpl
from main.service.utility.logger import log
from main.service.utility.mail import send_mail_confirm_email, send_mail_login_new_ip, send_mail_forgotten_password
from main.service.utility.utils import basic_regex, email_regex, passwd_regex


class UserImpl(BaseImpl):
    def __init__(self):
        super().__init__(UserFacade)

    def create(self, form):
        try:
            username = form.get('register-username')
            email = form.get('register-email')
            passwd = form.get('register-passwd')
            first_name = form.get('register-first-name')
            last_name = form.get('register-last-name')
            conditions = form.get('register-conditions')

            find_username = self.T.find(username, 'username')
            find_email = self.T.find(email, 'email')

            if (not basic_regex(username) or
                    not email_regex(email) or
                    not passwd_regex(passwd) or
                    not basic_regex(first_name) or
                    not basic_regex(last_name) or
                    not conditions or
                    find_username or
                    find_email):
                return Result(status=Status.BAD_REQUEST).response()

            passwd_hash = bcrypt.generate_password_hash(passwd).decode('utf-8')

            user = User(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=passwd_hash
            )

            if self.T.create(user):
                to_hash = f'{user.id}{user.date_joined}'
                token = bcrypt.generate_password_hash(to_hash).decode('utf-8')
                send_mail_confirm_email(msg_to=user.email, username=username, token=token)
                return result_handler(item=user)
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()

    def update(self, form, files):
        new_filename = ''
        try:
            username = form.get('profile-username')
            email = form.get('profile-email')
            passwd = form.get('profile-passwd')
            passwd_new = form.get('profile-passwd-new')
            first_name = form.get('profile-first-name')
            last_name = form.get('profile-last-name')
            date_of_birth = form.get('profile-date-of-birth')
            phone_number = form.get('profile-phone-number')
            image = files.get('profile-image')

            if not bcrypt.check_password_hash(current_user.password, passwd):
                return Result(status=Status.UNAUTHORIZED).response()

            find_username, find_email = False, False
            if current_user.username != username:
                find_username = self.T.find(value=username, column='username')
            if current_user.email != email:
                find_email = self.T.find(value=email, column='email')

            if (not basic_regex(username) or
                    not email_regex(email) or
                    not passwd_regex(passwd) or
                    not basic_regex(first_name) or
                    not basic_regex(last_name) or
                    find_username or
                    find_email):
                return Result(status=Status.BAD_REQUEST).response()

            if image and allowed_file(image.filename):
                filename = secure_filename(image.filename)
                basename, extension = os.path.splitext(filename)
                new_filename = f"{current_user.id}{extension}"
                image.save(os.path.join(f'{STATIC_DIR_PATH}/resources/user-images', new_filename))
                current_user.image = new_filename

            if passwd_new:
                current_user.password = bcrypt.generate_password_hash(passwd_new).decode('utf-8')

            current_user.username = username
            current_user.email = email
            current_user.first_name = first_name
            current_user.last_name = last_name
            current_user.date_of_birth = date_of_birth
            current_user.phone_number = phone_number

            db.session.commit()

            return Result().response()
        except Exception as e:
            os.remove(os.path.join(f'{STATIC_DIR_PATH}/resources/user-images', new_filename))
            db.session.rollback()
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()

    def login(self, form):
        try:
            username = form.get("login-username")
            password = form.get("login-passwd")
            remember = form.get('login-conditions')

            log.info(f'login: {username}')
            user = self.T.find(username, "username")

            if not user or not bcrypt.check_password_hash(user.password, password):
                return Result(status=Status.BAD_REQUEST).response()
            
            login_user(user, remember=True, duration=timedelta(days=365)) if remember else login_user(user)

            user.last_login_at = datetime.now()
            user.login_count += 1
            if 'X-Real-IP' in request.headers:
                if user.last_login_ip != request.headers['X-Real-IP']:
                    send_mail_login_new_ip(msg_to=current_user.email, ip_adress=request.headers['X-Real-IP'])
                user.last_login_ip = request.headers['X-Real-IP']
            else:
                if user.last_login_ip != request.remote_addr:
                    send_mail_login_new_ip(msg_to=current_user.email, ip_adress=request.remote_addr)
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

            return Result().response()
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()

    def logout(self):
        try:
            log.info(f'logout: {current_user.username}')
            logout_user()
            if request.cookies.get('archive'):
                response = make_response(redirect(request.referrer or url_for('template_api.index')))
                response.delete_cookie('archive')
                return response
            return redirect(request.referrer or url_for('template_api.index'))
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return redirect(request.referrer or url_for('template_api.index'))

    def confirm_email(self, email, token):
        try:
            user = self.T.find(email, "email")
            if user:
                secret = f'{user.id}{user.date_joined}'
                if bcrypt.check_password_hash(token, secret):
                    if not user.confirmed_at:
                        user.confirmed_at = datetime.now()
                        db.session.commit()
                    flash('email_confirmed')
                    return redirect(url_for('template_api.index'))
            flash('email_confirmation_failed')
            return redirect(url_for('template_api.index'))
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            flash('email_confirmation_failed')
            return redirect(url_for('template_api.index'))

    def generate_user_data(self, value, column):
        user = self.T.find(value=value, column=column)
        if not user:
            return result_handler(item=False)
        data = user.__repr__()
        image_path = f'{STATIC_DIR_PATH}/resources/user-images/{user.image}'
        with open(image_path, "rb") as img_file:
            image = str(base64.b64encode(img_file.read()))
        data['image_base64'] = image
        json_data = dumps(data, sort_keys=False, indent=4, ensure_ascii=False)
        response = Response(json_data, content_type='application/json')
        response.headers.set('Content-Disposition', 'attachment', filename='user_data.json')
        return response

    def forgotten_password(self, form):
        try:
            email = form.get('email')
            new_passwd = form.get('new-passwd')
            token = form.get('token')

            if token:
                user = self.T.find(value=email, column='email')
                current_time = datetime.now()
                timer_15 = user.forgot_passwd + timedelta(minutes=15)

                if not user or not passwd_regex(new_passwd) or timer_15 <= current_time:
                    return Result(status=Status.BAD_REQUEST).response()

                secret = f'{user.id}{user.forgot_passwd}'
                if bcrypt.check_password_hash(token, secret):
                    user.password = bcrypt.generate_password_hash(new_passwd).decode('utf-8')
                    db.session.commit()
                    return Result().response()

            elif email:
                user = self.T.find(value=email, column="email")
                if user:
                    user.forgot_passwd = datetime.now()
                    db.session.commit()
                    secret = f'{user.id}{user.forgot_passwd}'
                    token = bcrypt.generate_password_hash(secret).decode('utf-8')
                    send_mail_forgotten_password(msg_to=user.email, token=token)
                    return Result().response()
        except Exception as e:
            log.error(f'{e}', exc_info=True)
            return Result(status=Status.INTERNAL_SERVER_ERROR).response()




from datetime import datetime
from sqlalchemy.ext.associationproxy import association_proxy
from flask_login import UserMixin
from main.entities.core.base import db
from main.service.core.bcrypt import bcrypt
from main.service.utility.utils import repr_format_date


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column('id', db.Integer(), primary_key=True)
    first_name = db.Column('first_name', db.String(64), nullable=False)
    last_name = db.Column('last_name', db.String(64), nullable=False)
    email = db.Column('email', db.String(256), unique=True, nullable=False)
    username = db.Column('username', db.String(64), unique=True, nullable=False)
    password = db.Column('password', db.String(256), nullable=False)
    date_of_birth = db.Column('date_of_birth', db.Date())
    phone_number = db.Column('phone_number', db.String(16))
    image = db.Column('image', db.String(16))
    is_superuser = db.Column('is_superuser', db.Boolean)
    date_joined = db.Column('date_joined', db.DateTime())
    last_login_at = db.Column('last_login_at', db.DateTime())
    last_login_ip = db.Column('last_login_ip', db.String(16))
    last_seen = db.Column('last_seen', db.DateTime())
    login_count = db.Column('login_count', db.Integer)
    confirmed_at = db.Column('confirmed_at', db.DateTime())
    auth_token = db.Column('auth_token', db.String(256))
    forgot_passwd = db.Column('forgot_passwd', db.DateTime())

    reviews_association = db.relationship('Review', back_populates='user')
    reviews = association_proxy('reviews_association', 'movie')

    def __init__(self, first_name, last_name, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.date_of_birth = None
        self.phone_number = None
        self.image = None
        self.is_superuser = False
        self.date_joined = datetime.now()
        self.last_login_at = None
        self.last_login_ip = None
        self.last_seen = None
        self.login_count = 0
        self.confirmed_at = None
        self.auth_token = None
        self.forgot_passwd = None

    def __str__(self):
        return f'User(id={self.id}, username={self.username})'

    def __repr__(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "date_of_birth": repr_format_date(self.date_of_birth),
            "phone_number": self.phone_number,
            "image": self.image,
            "is_superuser": self.is_superuser,
            "date_joined": repr_format_date(self.date_joined),
            "last_login_at": repr_format_date(self.last_login_at),
            "last_login_ip": self.last_login_ip,
            "last_seen": repr_format_date(self.last_seen),
            "login_count": self.login_count,
            "confirmed_at": repr_format_date(self.confirmed_at),
            "auth_token": self.auth_token,
            "forgot_passwd": repr_format_date(self.forgot_passwd)
        }

    def generate_auth_token(self):
        to_hash = f'{self.id}{datetime.now()}'
        return bcrypt.generate_password_hash(to_hash).decode('utf-8')

    def ping(self):
        self.last_seen = datetime.now()
        db.session.add(self)
        db.session.commit()

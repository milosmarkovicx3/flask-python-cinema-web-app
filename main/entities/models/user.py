from datetime import datetime
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from sqlalchemy.ext.associationproxy import association_proxy

from main.entities.core.base import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column('id', db.Integer(), primary_key=True)
    first_name = db.Column('first_name', db.String(255), nullable=False)
    last_name = db.Column('last_name', db.String(255), nullable=False)
    email = db.Column('email', db.String(255), unique=True, nullable=False)
    username = db.Column('username', db.String(255), unique=True, nullable=False)
    password = db.Column('password', db.String(255), nullable=False)
    date_of_birth = db.Column('date_of_birth', db.DateTime())
    phone_number = db.Column('phone_number', db.String(255))
    image = db.Column('image', db.String(255))
    is_superuser = db.Column('is_superuser', db.Boolean)
    date_joined = db.Column('date_joined', db.DateTime())
    last_login_at = db.Column('last_login_at', db.DateTime())
    last_login_ip = db.Column('last_login_ip', db.String(255))
    last_seen = db.Column('last_seen', db.DateTime())
    login_count = db.Column('login_count', db.Integer)
    confirmed_at = db.Column('confirmed_at', db.DateTime())
    auth_token = db.Column('auth_token', db.String(255))

    reviews_association = db.relationship('Review', back_populates='user')
    reviews = association_proxy('reviews_association', 'movie')

    def __init__(self, first_name, last_name, email, username, password, date_of_birth=None, phone_number=None, image=None, is_superuser=False, date_joined=None, last_login_at=None, last_login_ip=None, last_seen=None, login_count=None, confirmed_at=None, auth_token=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.image = image
        self.is_superuser = is_superuser
        self.date_joined = date_joined
        self.last_login_at = last_login_at
        self.last_login_ip = last_login_ip
        self.last_seen = last_seen
        self.login_count = login_count
        self.confirmed_at = confirmed_at
        self.auth_token = auth_token

    def __str__(self):
        return str(self.__repr__())

    def __repr__(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "date_of_birth": str(self.date_of_birth),
            "phone_number": self.phone_number,
            "image": self.image,
            "is_superuser": self.is_superuser,
            "date_joined": str(self.date_joined),
            "last_login_at": str(self.last_login_at),
            "last_login_ip": self.last_login_ip,
            "last_seen": str(self.last_seen),
            "login_count": self.login_count,
            "confirmed_at": str(self.confirmed_at),
            "auth_token": self.auth_token
        }

    def generate_auth_token(self):
        data = (str(self.id) + self.username + str(datetime.now())).encode('utf-8')
        return pbkdf2_sha256.hash(data)

    def ping(self):
        self.last_seen = datetime.now()
        db.session.add(self)
        db.session.commit()
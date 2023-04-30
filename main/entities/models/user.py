from entities.core.base import db
from flask_login import UserMixin
from sqlalchemy import DateTime, Integer, String, Boolean


class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column('id', Integer(), primary_key=True)
    first_name = db.Column('first_name', String(255), nullable=False)
    last_name = db.Column('last_name', String(255), nullable=False)
    email = db.Column('email', String(255), unique=True, nullable=False)
    username = db.Column('username', String(255), unique=True, nullable=False)
    password = db.Column('password', String(255), nullable=False)
    date_of_birth = db.Column('date_of_birth', DateTime())
    phone_number = db.Column('phone_number', String(255))
    profile_picture = db.Column('profile_picture', String(255))
    is_superuser = db.Column('is_superuser', Boolean)
    date_joined = db.Column('date_joined', DateTime())
    last_login_at = db.Column('last_login_at', DateTime())
    last_login_ip = db.Column('last_login_ip', String(100))
    login_count = db.Column('login_count', Integer)
    confirmed_at = db.Column('confirmed_at', DateTime())

    def __init__(self, first_name, last_name, email, username, password, date_of_birth=None, phone_number=None, profile_picture=None, is_superuser=False, date_joined=None, last_login_at=None, last_login_ip=None, login_count=None, confirmed_at=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.username = username
        self.password = password
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.profile_picture = profile_picture
        self.is_superuser = is_superuser
        self.date_joined = date_joined
        self.last_login_at = last_login_at
        self.last_login_ip = last_login_ip
        self.login_count = login_count
        self.confirmed_at = confirmed_at

    def __str__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}, username={self.username}, password={self.password}, date_of_birth={self.date_of_birth}, phone_number={self.phone_number}, profile_picture={self.profile_picture}, is_superuser={self.is_superuser}, date_joined={self.date_joined}, last_login_at={self.last_login_at}, last_login_ip={self.last_login_ip}, login_count={self.login_count}, confirmed_at={self.confirmed_at})"

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
            "profile_picture": self.profile_picture,
            "is_superuser": self.is_superuser,
            "date_joined": str(self.date_joined),
            "last_login_at": str(self.last_login_at),
            "last_login_ip": self.last_login_ip,
            "login_count": self.login_count,
            "confirmed_at": str(self.confirmed_at)
        }

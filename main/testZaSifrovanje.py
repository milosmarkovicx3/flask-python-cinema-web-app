import binascii
import itertools
import secrets

from passlib.handlers.pbkdf2 import pbkdf2_sha256
from werkzeug.datastructures import ImmutableMultiDict


def encrypt(msg, key):
    cipher = xor_str(msg, key)
    return (binascii.hexlify(cipher.encode())).decode()

def decrypt(cipher, key):
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    return xor_str(cipher, key)

def xor_str(a, b):
    return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])

""" cipher = encrypt('Losmim123!', 'milos')
print(cipher)
masg = decrypt(cipher, 'milos')
print(masg) """



# print(secrets.token_urlsafe())
# print(secrets.SystemRandom().getrandbits(128))

#
# data = ImmutableMultiDict([('csrf_token', 'IjhiNDY0YmExM2RlYWFmZmMyYTFmNTg3MTk1MjE0Mjc0ZjM5MmQxNmUi.ZE3Wmg.9xWb0M9MvjYLS4rGCII4_gClBOs'), ('register-username', 'dwada'), ('register-email', 'dwad@dawd.faea'), ('register-passwd', 'rhrtt535!'), ('register-first-name', 'faef'), ('register-last-name', 'faefa'), ('register-conditions', 'on')])
# print(data['register-username'])
#
# class proba:
#     def __init__(self, first_name, last_name, email, username, password, date_of_birth=None, phone_number=None, profile_picture=None, is_superuser=False, date_joined=None, last_login_at=None, last_login_ip=None, login_count=None, confirmed_at=None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.username = username
#         self.password = password
#         self.date_of_birth = date_of_birth
#         self.phone_number = phone_number
#         self.profile_picture = profile_picture
#         self.is_superuser = is_superuser
#         self.date_joined = date_joined
#         self.last_login_at = last_login_at
#         self.last_login_ip = last_login_ip
#         self.login_count = login_count
#         self.confirmed_at = confirmed_at
#
#     def __str__(self):
#         return str(self.__repr__())
#
#     def __repr__(self):
#         return {
#             "first_name": self.first_name,
#             "last_name": self.last_name,
#             "email": self.email,
#             "username": self.username,
#             "password": self.password,
#             "date_of_birth": str(self.date_of_birth),
#             "phone_number": self.phone_number,
#             "profile_picture": self.profile_picture,
#             "is_superuser": self.is_superuser,
#             "date_joined": str(self.date_joined),
#             "last_login_at": str(self.last_login_at),
#             "last_login_ip": self.last_login_ip,
#             "login_count": self.login_count,
#             "confirmed_at": str(self.confirmed_at)
#         }
#
# print(proba("fa","faa","fafa","fafa","fa"))
# print(proba("fa","faa","fafa","fafa",'fa').__repr__())








hash = pbkdf2_sha256.hash("garden")
print(pbkdf2_sha256.verify("garden", hash))
print(pbkdf2_sha256.hash("gardengardengardengardengardengarden"))
import os

from passlib.handlers.pbkdf2 import pbkdf2_sha256

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

token = pbkdf2_sha256.hash('frontrunner'+str('2023-05-18 00:32:29'))

print(pbkdf2_sha256.verify(secret='frontrunner2023-05-18 00:32:29', hash=token))
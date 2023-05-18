import os

from passlib.handlers.pbkdf2 import pbkdf2_sha256

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')





print(pbkdf2_sha256.verify(secret='frontrunner'+'2023-05-18 05:22:45', hash='$pbkdf2-sha256$29000$O6eUMoawVkoJQUgphdA6Rw$VuTnMq51IK3cq5xkasKMDUxMJsxNLyeMbVNaE8DKS1I'))
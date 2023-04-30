import binascii
import itertools
import secrets

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


data = ImmutableMultiDict([('csrf_token', 'IjhiNDY0YmExM2RlYWFmZmMyYTFmNTg3MTk1MjE0Mjc0ZjM5MmQxNmUi.ZE3Wmg.9xWb0M9MvjYLS4rGCII4_gClBOs'), ('register-username', 'dwada'), ('register-email', 'dwad@dawd.faea'), ('register-passwd', 'rhrtt535!'), ('register-first-name', 'faef'), ('register-last-name', 'faefa'), ('register-conditions', 'on')])
print(data['register-username'])
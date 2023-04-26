import binascii
import itertools


def encrypt(msg, key):
    cipher = xor_str(msg, key)
    return (binascii.hexlify(cipher.encode())).decode()

def decrypt(cipher, key):
    cipher = (binascii.unhexlify(cipher.encode())).decode()
    return xor_str(cipher, key)

def xor_str(a, b):
    return ''.join([chr(ord(x)^ord(y)) for x, y in zip(a, itertools.cycle(b))])

cipher = encrypt('Losmim123!', 'milos')
print(cipher)
masg = decrypt(cipher, 'milos')
print(masg)


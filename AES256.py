# AES 256 encryption/decryption using pycrypto library

import base64
import hashlib
import os

from Crypto import Random
from Crypto.Cipher import AES


#   Pads the input with spaces to form a 16bit block
def pad(s):
    block_size = 16
    remainder = len(s) % block_size
    padding_needed = block_size - remainder
    return s + padding_needed * ' '


#   Removes the unnecessary padding
def unpad(s):
    return s.rstrip()


#   Generates a random Salt, IV
#   uses hashed private key to reduce intrusion
def encrypt(plain_text, password):
    salt = os.urandom(AES.block_size)
    iv = Random.new().read(AES.block_size)
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    padded_text = pad(plain_text)
    padded_text = padded_text.encode("utf8")
    cipher_config = AES.new(private_key, AES.MODE_CBC, iv)
    return {
        'cipher_text': base64.b64encode(cipher_config.encrypt(padded_text)),
        'salt': base64.b64encode(salt),
        'iv': base64.b64encode(iv)
    }


def decrypt(enc_dict, password):
    salt = base64.b64decode(enc_dict['salt'])
    enc = base64.b64decode(enc_dict['cipher_text'])
    iv = base64.b64decode(enc_dict['iv'])
    private_key = hashlib.scrypt(password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)
    cipher = AES.new(private_key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc)
    original = unpad(decrypted)
    return original.decode()


def main():
    password = "password"

    input = "First let us encrypt secret message"
    encrypted = encrypt(input, password)
    print(encrypted)

    decrypted = decrypt(encrypted, password)
    print(decrypted)
    # print(bytes.decode(decrypted))


main()

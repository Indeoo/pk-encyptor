import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def generate_key(password):
    salt = b'\x87\x12\xac\xa3\x91\xb9\xfe\xb4\x08\x0c\xac\x19\xc6d\x85'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def encrypt_private_key(private_key, password):
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.encrypt(private_key.encode())


def encrypt_private_keys(private_keys, password):
    return [encrypt_private_key(private_key, password) for private_key in private_keys]


def decrypt_private_key(encrypted_private_key, password):
    key = generate_key(password)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_private_key)


def decrypt_data(private_keys, password):
    return [decrypt_private_key(private_key, password) for private_key in private_keys]

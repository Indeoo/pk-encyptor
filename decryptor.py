from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

from encryptor import read_private_keys, write_data_to_file


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


def decrypt_private_key(encrypted_private_key, password):
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted_private_key = fernet.decrypt(encrypted_private_key)
    return decrypted_private_key


decrypted_data = []


if __name__ == '__main__':
    password = b'test'  # Здесь должна быть пользовательская фраза

    for private_key in read_private_keys('cryptography.txt'):
        decrypted_key = decrypt_private_key(private_key, password)
        decrypted_data.append(decrypted_key)

    write_data_to_file('decrypted_wallets.txt', decrypted_data)

    print("Дешифрование завершено. Приватные ключи сохранены в decrypted_wallets.txt.")

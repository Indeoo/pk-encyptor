from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
import base64

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
    encrypted_private_key = fernet.encrypt(private_key.encode())
    return encrypted_private_key


def read_private_keys(filename):
    with open(filename, 'r') as file:
        private_keys = file.readlines()
    private_keys = [key.strip() for key in private_keys]
    return private_keys


def write_data_to_file(filename, encrypted_data):
    with open(filename, 'w') as file:
        for encrypted_key in encrypted_data:
            file.write(encrypted_key.decode() + '\n')

encrypted_data = []

if __name__ == '__main__':
    password = b'test'  # Здесь должна быть пользовательская фраза

    for private_key in read_private_keys('wallets.txt'):
        encrypted_key = encrypt_private_key(private_key, password)
        encrypted_data.append(encrypted_key)

    write_data_to_file('cryptography.txt', encrypted_data)

    print("Шифрование завершено. Зашифрованные данные сохранены в cryptography.txt.")

from core.arguments_parser import parse_arguments
from core.data import read_private_keys, write_data_to_file
from core.utils import encrypt_private_keys

DECRYPTED_DATA_FILE = 'data/decrypted_data.txt'
ENCRYPTED_DATA_FILE = 'data/encrypted_data.txt'

PASSWORD = 'test'

if __name__ == '__main__':
    decrypted_data_file, password = parse_arguments(DECRYPTED_DATA_FILE, PASSWORD)

    encrypted_data = encrypt_private_keys(read_private_keys(decrypted_data_file), password)
    write_data_to_file(ENCRYPTED_DATA_FILE, encrypted_data)

    print(f"Шифрование завершено. Зашифрованные данные сохранены в {ENCRYPTED_DATA_FILE}.")

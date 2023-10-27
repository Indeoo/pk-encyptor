from core.arguments_parser import parse_arguments
from core.utils import decrypt_data
from encryptor import read_private_keys, write_data_to_file

ENCRYPTED_WALLETS_FILE = 'data/encrypted_data.txt'
DECRYPTED_DATA_FILE = 'data/decrypted_data.txt'

PASSWORD = 'test'

if __name__ == '__main__':
    encrypted_data_file, password = parse_arguments(ENCRYPTED_WALLETS_FILE, PASSWORD)

    decrypted_data = decrypt_data(read_private_keys(encrypted_data_file), password)

    write_data_to_file(DECRYPTED_DATA_FILE, decrypted_data)

    print(f"Дешифрование завершено. Приватные ключи сохранены в {DECRYPTED_DATA_FILE}.")

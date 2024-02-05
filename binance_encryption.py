from core.data import write_data_to_file, write_binance_api_to_file
from core.utils import encrypt_private_key

ENCRYPTED_DATA_FILE = 'data/encrypted_binance_api.txt'
PASSWORD = b'test'

if __name__ == '__main__':
    apiKey = 'test'
    secretKey = 'test'

    encrypted_binance_api = encrypt_private_key(f'{apiKey},{secretKey}', PASSWORD)
    write_binance_api_to_file(ENCRYPTED_DATA_FILE, encrypted_binance_api)

    print(f"Шифрование завершено. Зашифрованные данные сохранены в {ENCRYPTED_DATA_FILE}.")

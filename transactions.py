from cryptography.fernet import Fernet

def process_transaction(data, key):
    fernet = Fernet(key)
    try:
        decrypted_data = fernet.decrypt(data).decode()
        print(f"Processing transaction with data: {decrypted_data}")
    except Exception as e:
        print(f"Data integrity verification failed: {e}")

from cryptography.fernet import Fernet

def encrypt_data(data):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

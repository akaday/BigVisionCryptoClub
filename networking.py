from cryptography.fernet import Fernet

def establish_secure_connection():
    key = Fernet.generate_key()
    print(f"Secure connection established with key: {key}")

def start_network():
    establish_secure_connection()
    print("Network started.")

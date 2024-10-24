from p2p.networking import start_network
from p2p.encryption import encrypt_data
from p2p.transactions import process_transaction
from cryptography.fernet import Fernet

def main():
    start_network()
    data = "Hello, crypto club!"
    key = Fernet.generate_key()
    encrypted_data = encrypt_data(data, key)
    print(f"Encrypted Data: {encrypted_data}")
    process_transaction(encrypted_data)

if __name__ == "__main__":
    main()

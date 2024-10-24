from p2p.networking import start_network
from p2p.encryption import encrypt_data
from p2p.transactions import process_transaction

def main():
    start_network()
    data = "Hello, crypto club!"
    encrypted_data = encrypt_data(data)
    print(f"Encrypted Data: {encrypted_data}")
    process_transaction(encrypted_data)

if __name__ == "__main__":
    main()

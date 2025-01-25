from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import socket

def generate_dh_parameters():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    return parameters

def generate_dh_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_key(private_key, peer_public_key):
    shared_key = private_key.exchange(peer_public_key)
    derived_key = HKDF(
        algorithm=hashes.SHA256(),
        length=32,
        salt=None,
        info=b'handshake data',
        backend=default_backend()
    ).derive(shared_key)
    return derived_key

def establish_secure_connection():
    parameters = generate_dh_parameters()
    private_key, public_key = generate_dh_key_pair(parameters)
    
    # Simulate key exchange with peer
    peer_private_key, peer_public_key = generate_dh_key_pair(parameters)
    shared_key = derive_shared_key(private_key, peer_public_key)
    peer_shared_key = derive_shared_key(peer_private_key, public_key)
    
    assert shared_key == peer_shared_key, "Shared keys do not match!"
    
    print(f"Secure connection established with shared key: {shared_key}")

def encrypt_message(message, key):
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

def start_network():
    establish_secure_connection()
    print("Network started.")
    
    # Simulate sending and receiving encrypted messages
    message = "Hello, peer!"
    key = Fernet.generate_key()
    encrypted_message = encrypt_message(message, key)
    print(f"Encrypted message: {encrypted_message}")
    
    decrypted_message = decrypt_message(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

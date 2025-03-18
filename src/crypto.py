from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def encrypt_message(message, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    padded_message = message.encode() + b" " * (16 - len(message) % 16)
    return encryptor.update(padded_message) + encryptor.finalize()

def decrypt_message(ciphertext, key, iv):
    try:
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_message = decryptor.update(ciphertext) + decryptor.finalize()
        return padded_message.decode("utf-8").strip()
    except Exception as e:
        return None
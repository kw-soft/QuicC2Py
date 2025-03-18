from src.crypto import encrypt_message, decrypt_message

def test_encryption_decryption():
    key = b'\x00' * 32
    iv = b'\x00' * 16
    message = "Test message"
    encrypted = encrypt_message(message, key, iv)
    decrypted = decrypt_message(encrypted, key, iv)
    assert decrypted == message
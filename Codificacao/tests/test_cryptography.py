import pytest
from cryptography.fernet import Fernet
from app.services.cryptographyService.cryptography import Cryptography

# Teste para verificar se a chave de criptografia está sendo gerada corretamente
def test_generate_key():
    crypto = Cryptography()
    key = crypto.generateKey()
    assert isinstance(key, bytes)
    assert len(key) == 44

# Teste para verificar se o texto está sendo criptografado corretamente
def test_encrypt_text():
    crypto = Cryptography()
    key = crypto.generateKey()
    text = "hello"
    encrypted_text = crypto.encryptText(text, key)
    assert isinstance(encrypted_text, bytes)

# Teste para verificar se o texto criptografado está sendo descriptografado corretamente
def test_decrypt_text():
    crypto = Cryptography()
    key = crypto.generateKey()
    text = "hello"
    encrypted_text = crypto.encryptText(text, key)
    decrypted_text = crypto.decryptText(encrypted_text, key)
    assert decrypted_text == text

# Teste para verificar se a senha está sendo hashada corretamente
def test_hash_password():
    crypto = Cryptography()
    password = "password123"
    hashed_password = crypto.hashPassword(password)
    assert isinstance(hashed_password, str)
    assert len(hashed_password) == 64


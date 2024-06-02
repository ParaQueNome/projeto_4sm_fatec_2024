from unittest.mock import Mock
from app.services.cryptographyService.cryptographyService import CryptographyService

def test_encrypt_password():
    # Criando um mock para a classe Cryptography
    crypto_mock = Mock()

    # Configurando o comportamento do mock
    crypto_mock.hashPassword.return_value = "hashed_password"
    crypto_mock.generateKey.return_value = "encryption_key"
    crypto_mock.encryptText.return_value = "encrypted_password"

    # Instanciando o serviço CryptographyService com o mock
    crypto_service = CryptographyService(crypto_mock)

    # Chamando o método encryptPassword
    encrypted_password, key = crypto_service.encryptPassword("password123")

    # Verificando se os métodos do mock foram chamados corretamente
    crypto_mock.hashPassword.assert_called_once_with("password123")
    crypto_mock.generateKey.assert_called_once()
    crypto_mock.encryptText.assert_called_once_with("hashed_password", "encryption_key")

    # Verificando se o resultado é o esperado
    assert encrypted_password == "encrypted_password"
    assert key == "encryption_key"

def test_decrypt_password():
    # Criando um mock para a classe Cryptography
    crypto_mock = Mock()

    # Configurando o comportamento do mock
    crypto_mock.decryptText.return_value = "decrypted_password"

    # Instanciando o serviço CryptographyService com o mock
    crypto_service = CryptographyService(crypto_mock)

    # Chamando o método decryptPassword
    decrypted_password = crypto_service.decryptPassword("encrypted_password", "encryption_key")

    # Verificando se o método do mock foi chamado corretamente
    crypto_mock.decryptText.assert_called_once_with("encrypted_password", "encryption_key")

    # Verificando se o resultado é o esperado
    assert decrypted_password == "decrypted_password"

def test_hash_confirm_password():
    # Criando um mock para a classe Cryptography
    crypto_mock = Mock()

    # Configurando o comportamento do mock
    crypto_mock.hashPassword.return_value = "hashed_password"

    # Instanciando o serviço CryptographyService com o mock
    crypto_service = CryptographyService(crypto_mock)

    # Chamando o método hashConfirmPassword
    hashed_password = crypto_service.hashConfirmPassword("password123")

    # Verificando se o método do mock foi chamado corretamente
    crypto_mock.hashPassword.assert_called_once_with("password123")

    # Verificando se o resultado é o esperado
    assert hashed_password == "hashed_password"

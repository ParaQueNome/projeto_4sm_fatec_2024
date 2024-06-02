from unittest.mock import Mock
from app.services.authenticationService.signup import SignUp

def test_signup():
    # Mock para ConexaoRepository
    conexao_mock = Mock()
    conexao_mock.insert.return_value = True

    # Mock para CryptographyService
    crypto_mock = Mock()
    crypto_mock.encryptPassword.return_value = ("encrypted_password", "encryption_key")

    # Instanciando o serviço SignUp com os mocks
    signup_service = SignUp(conexao_mock, crypto_mock)

    # Dados para o cadastro
    data = {
        "username": "user123",
        "password": "password123"
    }

    # Chamando a função signup
    result = signup_service.signup(data)

    # Verificando se a inserção foi feita corretamente
    assert result is True
    conexao_mock.insert.assert_called_once_with("usuario", username="user123", password="encrypted_password", key="encryption_key")

def test_close_account():
    # Mock para ConexaoRepository
    conexao_mock = Mock()
    conexao_mock.delete.return_value = None

    # Mock para CryptographyService
    crypto_mock = Mock()

    # Instanciando o serviço SignUp com os mocks
    signup_service = SignUp(conexao_mock, crypto_mock)

    # Dados para o fechamento da conta
    data = {
        "username": "user123"
    }

    # Chamando a função closeAccount
    signup_service.closeAccount(data)

    # Verificando se a deleção foi feita corretamente
    conexao_mock.delete.assert_called_once_with("usuario", username="user123")

from unittest.mock import Mock
from flask import session
from app.services.authenticationService.login import Login

def test_signin():
    # Mock para ConexaoRepository
    conexao_mock = Mock()
    conexao_mock.select.return_value = {
        'username': 'user123',
        'email': 'user@example.com',
        'password': 'hashed_password',
        'key': 'encryption_key'
    }

    # Mock para CryptographyService
    crypto_mock = Mock()
    crypto_mock.decryptPassword.return_value = 'password123'
    crypto_mock.hashConfirmPassword.return_value = 'hashed_password'

    # Configurando a sessão Flask
    session = {}

    # Instanciando o serviço Login com os mocks
    login_service = Login(conexao_mock, crypto_mock)

    # Dados para o login
    data = {
        "email": "user@example.com",
        "password": "password123"
    }

    # Chamando a função signIn
    result = login_service.signIn(data)

    # Verificando se o login foi bem-sucedido
    assert result is True
    assert session['usuario'] == 'user123'
    assert session['email'] == 'user@example.com'

def test_signout():
    # Configurando a sessão Flask
    session = {'usuario': 'user123', 'email': 'user@example.com'}

    # Instanciando o serviço Login
    login_service = Login(Mock(), Mock())

    # Chamando a função signOut
    login_service.signOut()

    # Verificando se a sessão foi limpa
    assert 'usuario' not in session
    assert 'email' not in session

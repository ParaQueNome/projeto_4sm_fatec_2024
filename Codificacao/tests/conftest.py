# tests/conftest.py

import pytest
import mongomock
from app import create_app
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

class MockConfig:
    def getConnection(self):
        return mongomock.MongoClient()

@pytest.fixture
def db():
    config = MockConfig()
    conexao = Conexao(config, "test_db")
    yield conexao
    conexao.closeConnection()

@pytest.fixture
def db():
    config = MockConfig()
    conexao = Conexao(config, "test_db")
    yield conexao
    conexao.closeConnection()
    
@pytest.fixture
def repository(db):
    return ConexaoRepository(db)
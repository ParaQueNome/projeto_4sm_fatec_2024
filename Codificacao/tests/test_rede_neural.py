import pytest
import numpy as np
from app.services.financeService.RedeNeuralService import RedeNeuralService

@pytest.fixture
def neural_service():
    return RedeNeuralService()

def test_preview(neural_service):
    # Dados de entrada
    dados = [1, 2, 3, 4, 5]

    # Chamar o método preview
    resultado = neural_service.preview(dados)

    # Verificar se o resultado é uma instância de ndarray (numpy array)
    assert isinstance(resultado, np.ndarray)

    # Verificar se o resultado tem o mesmo shape que esperamos
    assert resultado.shape == (1,)  # Assumindo que a rede neural retorna um único valor

    # Outros testes de asserção conforme necessário
    # assert ...


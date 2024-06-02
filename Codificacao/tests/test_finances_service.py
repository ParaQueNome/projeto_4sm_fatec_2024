from unittest.mock import Mock
from app.services.financeService.FinanceService import FinanceService
from bson import ObjectId

def test_inserir_receitas():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Dados para inserir uma receita
    email = "user@example.com"
    data = {"descricao": "Salário", "renda": 3000.0}

    # Chamando o método inserirReceitas
    finance_service.inserirReceitas(email, data)

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with('usuario', email=email)
    conexao_mock.insertDespesas.assert_called_once()

def test_exibir_financas():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Configurando o comportamento do mock
    conexao_mock.select.return_value = {
        'despesas': {
            'receitas': [{'descricao': 'Salário', 'renda': 3000.0}],
            'gastos': [{'descricao': 'Aluguel', 'valor': 1000.0}]
        }
    }

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Chamando o método exibirFinancas
    financas = finance_service.exibirFinancas("user@example.com")

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with('usuario', email="user@example.com")

    # Verificando se os dados de finanças foram retornados corretamente
    assert financas == {
        'receitas': [{'descricao': 'Salário', 'renda': 3000.0}],
        'gastos': [{'descricao': 'Aluguel', 'valor': 1000.0}]
    }

# Testes para outros métodos da classe FinanceService podem ser escritos de forma semelhante
def test_inserir_gastos():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Dados para inserir um gasto
    email = "user@example.com"
    data = {"descricao": "Aluguel", "valor": 1000.0}

    # Chamando o método inserirGastos
    finance_service.inserirGastos(email, data)

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with('usuario', email=email)
    conexao_mock.insertDespesas.assert_called_once()

def test_deletar_receita():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Configurando o comportamento do mock para o método select
    conexao_mock.select.return_value = {"_id": ObjectId(), "email": "user@example.com"}

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Chamando o método deletarReceita com um ObjectId válido
    finance_service.deletarReceita("user@example.com", ObjectId())

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with('usuario', email="user@example.com")
    conexao_mock.executeAggregation.assert_called_once()

def test_deletar_despesa():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Configurando o comportamento do mock para o método select
    conexao_mock.select.return_value = {"_id": ObjectId(), "email": "user@example.com"}

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Chamando o método deletarDespesa com um ObjectId válido
    finance_service.deletarDespesa("user@example.com", ObjectId())

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with('usuario', email="user@example.com")
    conexao_mock.executeAggregation.assert_called_once()

def test_total_gastos():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Configurando o comportamento do mock
    conexao_mock.select.return_value = {
        'despesas': {'gastos': [{'valor': 500}, {'valor': 750}]}
    }

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Chamando o método totalGastos
    total = finance_service.totalGastos("user@example.com")

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with("usuario", email="user@example.com")

    # Verificando se o total de gastos foi calculado corretamente
    assert total == 1250

def test_total_receitas():
    # Criando um mock para o repositório de conexão
    conexao_mock = Mock()

    # Configurando o comportamento do mock
    conexao_mock.select.return_value = {
        'despesas': {'receitas': [{'renda': 2000}, {'renda': 1500}]}
    }

    # Instanciando o serviço FinanceService com o mock
    finance_service = FinanceService(conexao_mock)

    # Chamando o método totalReceitas
    total = finance_service.totalReceitas("user@example.com")

    # Verificando se o método do mock foi chamado corretamente
    conexao_mock.select.assert_called_once_with("usuario", email="user@example.com")
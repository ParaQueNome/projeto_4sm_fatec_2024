from app.repositories.ConexaoRepository import ConexaoRepository

class FinanceService:

    def __init__(self, conexaoRepository: ConexaoRepository ) -> None:
        self.conexao = conexaoRepository

    def inserirReceitas(self, email, data):
        data_email = {'email':email}
        condicao = self.conexao.select('usuario', **data_email)
        vetor = {'despesas.receitas': data}
        self.conexao.insertDespesas('usuario',condicao,**vetor)

    def inserirGastos(self, email, data):
        data_email = {'email': email}
        condicao = self.conexao.select('usuario', **data_email)
        vetor = {'despesas.gastos': data}
        self.conexao.insertDespesas('usuario', condicao, **vetor)

    def exibirFinancas(self, email):
        data_email = {'email':email}
        dados = self.conexao.select('usuario', **data_email)
        return dados['despesas']

    def totalGastos(self, usuario):
        dados = self.conexao.select("usuario", **usuario)
        for despesas in dados['despesas.gastos']:
            total = despesas['valor'] + total
        return total

from app.repositories.ConexaoRepository import ConexaoRepository

class FinanceService:

    def __init__(self, conexaoRepository: ConexaoRepository ) -> None:
        self.conexao = conexaoRepository

    def inserirGastos(self, usuario, data):
        condicao = self.conexao.select('usuario', usuario).get('email')
        self.conexao.insertDespesas('usuario',condicao,**data)

    def exibirFinancas(self, usuario):
        dados = self.conexao.select('usuario', **usuario)
        return dados

    def totalGastos(self, usuario):
        dados = self.conexao.select("usuario", **usuario)

from app.repositories.ConexaoRepository import ConexaoRepository
from bson import ObjectId

# Classe responsavel por validar e realizar o crud dos dados financeiros do usuario
class FinanceService:
    
    def __init__(self, conexaoRepository: ConexaoRepository ) -> None:
        self.conexao = conexaoRepository

    def inserirReceitas(self, email, data):
        data_email = {'email':email}
        condicao = self.conexao.select('usuario', **data_email)
        data['_id'] = ObjectId()
        vetor = {'despesas.receitas': data}
        self.conexao.insertDespesas('usuario',condicao,**vetor)

    def inserirGastos(self, email, data):
        data_email = {'email': email}
        condicao = self.conexao.select('usuario', **data_email)
        id = ObjectId()
        data['_id'] = ObjectId()
        vetor = {'despesas.gastos': data}
        self.conexao.insertDespesas('usuario', condicao, **vetor)

    def exibirFinancas(self, email):
        data_email = {'email':email}
        dados = self.conexao.select('usuario', **data_email)
        return dados['despesas']
    def deletarReceita(self, email, idReceita):
        dictEmail = {'email': email}
        condicao = self.conexao.select('usuario', **dictEmail)
        query = {'_id': condicao['_id']}
        update = {'$pull': {'despesas.receitas': {'_id': ObjectId(idReceita)}}}
        kwargs = [query, update]  # Combinar os dicionários
        self.conexao.executeAggregation('usuario', kwargs)
    
    def deletarDespesa(self, email, idDespesa):
        dictEmail = {'email':email}
        condicao = self.conexao.select('usuario', **dictEmail)
        query = {'_id': condicao['_id']}
        update = {'$pull': {'despesas.gastos':{'_id':ObjectId(idDespesa)}}}
        kwargs = [query, update]
        self.conexao.executeAggregation('usuario', kwargs)
    
    def totalGastos(self, usuario):
        dictEmail = {'email': usuario}
        dados = self.conexao.select("usuario", **dictEmail)
        print(dados)
        despesas = dados['despesas']
        descontos = despesas['gastos']
        total = 0
        for desconto in descontos:
            castGasto = float(desconto['valor'])
            total = castGasto + total
        return total
    
    def totalReceitas(self, usuario):
        dictEmail = {'email': usuario}
        dados = self.conexao.select("usuario", **dictEmail)
        despesas = dados['despesas']
        receitas = despesas['receitas']
        total = 0
        for receita in receitas:
            castReceita = float(receita['renda'])
            total = castReceita + total
        return total
    
    def updateDespesas(self, email, idDespesa, **gastos):
        dictEmail = {'email': email}
        condicao = self.conexao.select('usuario', **dictEmail)
        query = {'_id': condicao['_id'], 'despesas.gastos._id': ObjectId(idDespesa)}
        update = {'$set': {'despesas.gastos.$':gastos}}
        kwargs = [query, update]
        self.conexao.executeAggregation('usuario', kwargs)


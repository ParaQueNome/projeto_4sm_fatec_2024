from app.models.conexao_mongo import Conexao


class ConexaoRepository:
    def __init__(self, conexao : Conexao) -> None:
        self.conexao = conexao
    

    def insert(self, collection_name, **kwargs):
        self.conexao.insert(collection_name, **kwargs)

    def update(self, collection_name, **kwargs):
        self.conexao.update(collection_name, **kwargs)

    def delete(self, collection_name, **kwargs):
        self.conexao.delete(collection_name, **kwargs)

    def select(self, collection_name, **kwargs):
        return self.conexao.select(collection_name, **kwargs)
    
    def insertDespesas(self, collection_name,condicao, **kwargs):
        return self.conexao.insertDespesas(collection_name, condicao, **kwargs)
    
    def executeAggregation(self, collection_name,kwargs):
        return self.conexao.executeAggregation(collection_name,kwargs)
        
from app.repositories.ConexaoRepository import ConexaoRepository
from flask import sessions


class Login:

    def __init__(self, conexaoRepository: ConexaoRepository) -> None:
        self.conexao = conexaoRepository

    def signIn(self, data): 
        dados = self.conexao.select('usuario', **data)
        if dados:
            sessions['usuario'] = dados['nickname']
            sessions['email'] = dados['email']
            return True
    def signOut(self):
        sessions.clear()
        return True
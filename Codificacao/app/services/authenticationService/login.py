from app.repositories.ConexaoRepository import ConexaoRepository
from flask import sessions


class Login:

    def __init__(self, conexaoRepository: ConexaoRepository) -> None:
        self.conexao = conexaoRepository

    def login(self, data): 
        dados = self.conexao.select('usuario', **data)

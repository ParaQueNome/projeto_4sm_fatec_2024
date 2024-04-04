from app.repositories.ConexaoRepository import ConexaoRepository


class SignUp:

    def __init__(self, conexaoRepository: ConexaoRepository) -> None:
        self.conexao = conexaoRepository

    def cadastrar(self, data):
        print(data)
        self.conexao.insert("usurio", **data)
    
    def remover_cadastro(self, data : dict):
        self.conexao.delete("usurio", **data)
        
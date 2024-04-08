from app.repositories import ConexaoRepository
from app.services.cryptographyService.cryptographyService import CryptographyService


class SignUp:

    def __init__(self, conexaoRepository: ConexaoRepository, crypto: CryptographyService) -> None:
        self.conexao = conexaoRepository
        self.crypto = crypto
        

    def signup(self, data):
        password = str(data['password'])
        encryptedPassword = self.crypto.encryptPassword(password)
        data["password"] = encryptedPassword[0]
        data["key"] = encryptedPassword[1]
        self.conexao.insert("usuario", **data)
        return True
    
    def closeAccount(self, data : dict):
        self.conexao.delete("usuario", **data)
        
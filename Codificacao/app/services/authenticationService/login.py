from app.repositories.ConexaoRepository import ConexaoRepository
from app.services.cryptographyService.cryptographyService import CryptographyService
from flask import session


class Login:

    def __init__(self, conexaoRepository: ConexaoRepository, crypt= CryptographyService) -> None:
        self.conexao = conexaoRepository
        self.crypt = crypt

    def signIn(self, data):
        data_email = {'email': data['email']}
        print(data_email)
        dados = self.conexao.select('usuario', **data_email)
        print(dados)
        if dados:
            hashPassword = dados['password']
            key = dados['key']
            decrypetdPassword = self.crypt.decryptPassword(hashPassword,key)
            confirPass = self.crypt.hashConfirmPassword(data['password'])
            print(confirPass)
            print(decrypetdPassword)
            if confirPass == decrypetdPassword:
                session['usuario'] = dados['username']
                session['email'] = dados['email']
                return True
            
            return False
        
    def signOut(self):
        session.clear()
    
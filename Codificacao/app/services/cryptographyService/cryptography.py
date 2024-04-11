from cryptography.fernet import Fernet
import hashlib

class Cryptography:
    # Função para criar uma chave de criptografia
    def generateKey(self):
        return Fernet.generate_key()

    # Função para criptografar um texto usando uma chave
    def encryptText(self,text, key):
        cipher_suite = Fernet(key)
        return cipher_suite.encrypt(text.encode())

    # Função para descriptografar um texto usando uma chave
    def decryptText(self,encrypted_text, key):
        cipher_suite = Fernet(key)
        return cipher_suite.decrypt(encrypted_text).decode()
    

    # Função para criar um hash seguro de uma senha
    def hashPassword(self,password):
        return hashlib.sha256(password.encode()).hexdigest()

    

from pymongo import MongoClient


class Config:
    def __init__(self, db_name : str) -> None:
        try:
            # Inicializando a conexão com o MongoDB Atlas
            self.client = MongoClient('mongodb+srv://guiaugusto455:UnvhSbCJ165OSooP@cluster0.nlhzemu.mongodb.net/')
            self.db = self.client[db_name]
            print('Conexão com o MongoDB Atlas estabelecida com sucesso!')
        except Exception as e:
            print('Erro ao conectar ao MongoDB Atlas:', e)



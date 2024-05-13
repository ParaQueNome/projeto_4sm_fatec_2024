
from pymongo import MongoClient


class Config:
    def __init__(self) -> None:
        try:
            # Inicializando a conexão com o MongoDB Atlas
            #self.client = MongoClient('mongodb+srv://guiaugusto455:UnvhSbCJ165OSooP@cluster0.nlhzemu.mongodb.net/')
            self.client = MongoClient('mongodb://localhost:27017')
        except Exception as e:
            print('Erro ao conectar ao MongoDB Atlas:', e)
            
    def getConnection(self):
        return self.client




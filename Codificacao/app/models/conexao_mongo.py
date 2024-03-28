from config import Config

class Conexao: 
    def __init__(self, connection: Config, db_name:str):
        self.client = connection.getConnection()
        self.db = self.client[db_name]
        
    
    def insert(self,collection_name, **kwargs)-> None:
        data = {}
        collection = self.db[collection_name]
        for key, value in kwargs.items():
            data[key] = value
            
        collection.insert_one(data)
        
        
    
    
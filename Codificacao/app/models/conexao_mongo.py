from config import Config

class Conexao: 
    def __init__(self, connection: Config, db_name:str):
        self.client = connection.getConnection()
        self.db = self.client[db_name]
        
    
    def insert(self,collection_name, **kwargs)-> None:
        collection = self.db[collection_name]
            
        collection.insert_one(kwargs)

    def update(self ,collection_name, **kwargs)-> None:
    
        collection = self.db[collection_name]

        collection.update_one(kwargs)
    
    def delete(self, collection_name, **kwargs)-> None:
       
        collection = self.db[collection_name]

        collection.delete_one(kwargs)
    
    def select(self, collection_name, **kwargs)-> list:
        
        collection = self.db[collection_name]
        

        return collection.find(kwargs)
        
    
    
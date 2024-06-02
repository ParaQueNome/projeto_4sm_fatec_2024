from config import Config

class Conexao: 
    def __init__(self, connection: Config, db_name:str):
        self.client = connection.getConnection()
        self.db = self.client[db_name]
        
    
    def insert(self,collection_name, **kwargs)-> None:
        collection = self.db[collection_name]
            
        collection.insert_one(kwargs)

    def insertDespesas(self, collection_name,condicao, **kwargs) -> None:
        collection = self.db[collection_name]
        collection.update_one(condicao, {'$push': kwargs}, upsert=True)
    
    def delete(self, collection_name, **kwargs)-> None:
       
        collection = self.db[collection_name]

        collection.delete_one(kwargs)
    
    def select(self, collection_name, **kwargs)-> list:
        
        collection = self.db[collection_name]
        

        return collection.find_one(kwargs)
    
    def executeAggregation(self, collection_name ,kwargs ):
        collection = self.db[collection_name]
        filter = kwargs[0]
        update= kwargs[1]
        collection.update_one(filter = filter, update =update)
        
    def closeConnection(self):
        self.client.close()
    
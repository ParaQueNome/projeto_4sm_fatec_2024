import os
from dotenv import load_dotenv
from polygon import RESTClient

class PolygonApiService:

    def __init__(self) -> None:
        load_dotenv()
        client = RESTClient(api_key=os.getenv("POLYGON_API_KEY"))
    
    def carregarAcoes(self):
        

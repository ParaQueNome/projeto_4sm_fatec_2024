import os
from dotenv import load_dotenv
from polygon import RESTClient
from datetime import datetime, timedelta

class PolygonApiService(RESTClient):

    def __init__(self) -> None:
        load_dotenv()
        super().__init__(api_key=os.getenv("POLYGON_API_KEY"))
    
    def carregarAcoes(self):
        return self.get_grouped_daily_aggs((datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))
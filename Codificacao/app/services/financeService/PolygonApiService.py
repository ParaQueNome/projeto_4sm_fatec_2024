import os
from dotenv import load_dotenv
from polygon import RESTClient
from datetime import datetime, timedelta
import requests
class PolygonApiService(RESTClient):

    def __init__(self) -> None:
        load_dotenv()
        super().__init__(api_key=os.getenv("POLYGON_API_KEY"))
    
    def carregarAcoes(self):
        date_to_check = datetime.now()
        # Se hoje é sábado (5) ou domingo (6), buscar a data da última sexta-feira
        if date_to_check.weekday() == 6:  # Sunday
            date_to_check -= timedelta(days=2)
        else:
            # Se não for fim de semana, buscar a data do dia anterior
            date_to_check -= timedelta(days=1)
        exchanges = {}
        dailyExchanges = self.get_grouped_daily_aggs(date_to_check.strftime('%Y-%m-%d'))
        tickerDetails = requests.get('https://api.polygon.io/v3/reference/tickers?active=true&limit=100&apiKey=4U16LvuqPJUR1B8gFpAASREdkEqhdVoH')
        for ticker in tickerDetails.json()['results']:
            exchange = []
            for price in dailyExchanges:
                if price.ticker == ticker['ticker']:
                    exchange.append(ticker['name'])
                    exchange.append(price)
                    exchanges[price.ticker] = exchange

        return exchanges
        
    
    
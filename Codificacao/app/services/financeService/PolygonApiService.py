import os
from dotenv import load_dotenv
from polygon import RESTClient
from datetime import datetime, timedelta
import requests
class PolygonApiService(RESTClient):

    def __init__(self) -> None:
        load_dotenv()
        super().__init__(api_key=os.getenv("POLYGON_API_KEY"))

    def _getDiaUtil(self, dateToCheck):
        response = requests.get('https://api.polygon.io/v1/marketstatus/upcoming?apiKey=4U16LvuqPJUR1B8gFpAASREdkEqhdVoH')
        feriados = response.json()
        for feriado in feriados:
            if feriado['date'] == dateToCheck.strftime('%Y-%m-%d'):
                dateToCheck -= timedelta(days=1)
            
        if dateToCheck.weekday() == 6:  # Sunday
            dateToCheck -= timedelta(days=2)
        elif dateToCheck.weekday() == 0:  # Monday
            dateToCheck -= timedelta(days=3)
        
        return dateToCheck

    
    def carregarAcoes(self):
        dateToCheck = self._getDiaUtil(datetime.now() - timedelta(days=1))
        exchanges = {}
        dailyExchanges = self.get_grouped_daily_aggs(dateToCheck.strftime('%Y-%m-%d'))
        tickerDetails = requests.get('https://api.polygon.io/v3/reference/tickers?active=true&limit=1000&apiKey=4U16LvuqPJUR1B8gFpAASREdkEqhdVoH')
        for ticker in tickerDetails.json()['results']:
            exchange = {}
            for price in dailyExchanges:
                if price.ticker == ticker['ticker']:
                    exchange["name"] = ticker['name']
                    exchange["ticker"] = price.ticker
                    exchange["open"] = price.open
                    exchange["high"] = price.high
                    exchange["low"] = price.low
                    exchange["close"] = price.close
                    exchange["volume"] = price.volume
                    exchange["vwap"] = price.vwap
                    exchange["transactions"] = price.transactions
                    exchanges[price.ticker] = exchange

        return exchanges
    
    def tickerNews(self):
        response = requests.get("https://api.polygon.io/v2/reference/news?limit=100&apiKey=4U16LvuqPJUR1B8gFpAASREdkEqhdVoH")
        formDict = {}
        for ticker in response.json()['results']:
           rawDict = {}
           rawDict["publisher"] = ticker['publisher']
           rawDict["title"] = ticker['title']
           rawDict["author"] = ticker['author']
           rawDict["published_utc"] = ticker['published_utc']
           rawDict["article_url"] = ticker['article_url']
           rawDict["tickers"] = ticker['tickers']
           rawDict["image_url"] = ticker['image_url']
           rawDict["description"] = ticker['description']
           formDict[ticker['id']] = rawDict


        return formDict
    
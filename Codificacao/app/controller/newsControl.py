from flask import Blueprint, request
from flask import render_template
from app.services.financeService.PolygonApiService import PolygonApiService
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=15000, ttl=3600)  # Cache de 1 hora
newsBp = Blueprint('news', __name__, template_folder='templates/trades')

@cached(cache)
def getTickerNews():
    return PolygonApiService().tickerNews()

@newsBp.route('/dairy', methods=['GET'])
def news():

    newsService = getTickerNews()
    
    # Obter a página atual a partir dos parâmetros da query
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Número de itens por página

    # Paginação
    total_items = len(newsService)
    start = (page - 1) * per_page
    end = start + per_page  
    items = {k: newsService[k] for k in list(newsService)[start:end]}

    return render_template('trades/news.html', news=items, page=page, total_pages=(total_items // per_page) + 1)

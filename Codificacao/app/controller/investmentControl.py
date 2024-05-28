from flask import Blueprint, request, render_template, redirect, url_for, session
from app.services.financeService.PolygonApiService import PolygonApiService
from cachetools import cached, TTLCache

investmentBp = Blueprint('trade', __name__, template_folder='templates/trades')
cache = TTLCache(maxsize=15000, ttl=3600)  # Cache de 60 segundos
@cached(cache)
def getExchangeDetails():
    return PolygonApiService().carregarAcoes()

@investmentBp.route('/investment', methods=['GET', 'POST'])
def investment():
    
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    exchangeDetails = getExchangeDetails()
    # Obter a página atual a partir dos parâmetros da query
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Número de itens por página

    # Paginação
    total_items = len(exchangeDetails)
    start = (page - 1) * per_page
    end = start + per_page
    items = {k: exchangeDetails[k] for k in list(exchangeDetails)[start:end]}

    return render_template('trades/trade.html', exchange=items, page=page, total_pages=(total_items // per_page) + 1)
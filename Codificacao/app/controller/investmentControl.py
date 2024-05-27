from flask import Blueprint, request, render_template, redirect, url_for, session
from app.services.financeService.PolygonApiService import PolygonApiService

investmentBp = Blueprint('trade', __name__, template_folder='templates/trades')

@investmentBp.route('/investment', methods=['GET', 'POST'])
def investment():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))

    # Obter a página atual a partir dos parâmetros da query
    page = request.args.get('page', 1, type=int)
    per_page = 10  # Número de itens por página

    # Carregar as ações
    service = PolygonApiService()
    exchange_details = service.carregarAcoes()

    # Paginação
    total_items = len(exchange_details)
    start = (page - 1) * per_page
    end = start + per_page
    items = {k: exchange_details[k] for k in list(exchange_details)[start:end]}

    return render_template('trades/trade.html', exchange=items, page=page, total_pages=(total_items // per_page) + 1)

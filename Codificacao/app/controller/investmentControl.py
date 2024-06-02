from flask import Blueprint, json, request, render_template, redirect, url_for, session
import requests
from config import Config
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository
from app.services.financeService.PolygonApiService import PolygonApiService
from app.services.financeService.RedeNeuralService import RedeNeuralService
from app.services.opeaiApiService.openaiApi import OpenAiClient
from app.services.financeService.FinanceService import FinanceService
from cachetools import cached, TTLCache
from flask import jsonify

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


@investmentBp.route('/neural', methods = ['GET', 'POST'])
def neural():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    if request.method =='POST':
        data = request.json
        details = data.get('details')
        details = json.loads(details)
        dados = [[details.get('close'), details.get('open'), details.get('high'), details.get('low'), details.get('volume')]]
        regressor = RedeNeuralService().preview(dados)
        exchanges = {'empresa': details.get('name'), 'regressor': regressor }
        print(session.get('email'))
        openAi = OpenAiClient().userExchanges(
            FinanceService(ConexaoRepository(Conexao(Config(), 'Financia'))).totalReceitas(session.get('email')),
            FinanceService(ConexaoRepository(Conexao(Config(),'Financia'))).totalGastos(session.get('email')),
            session.get('usuario'),
            **exchanges)
        
        
        return jsonify({'details': openAi})
    return redirect(url_for('trade.investment'))
    


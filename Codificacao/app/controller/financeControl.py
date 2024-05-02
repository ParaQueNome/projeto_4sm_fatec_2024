from flask import Blueprint, request
from flask import render_template, redirect
from config import Config
from flask import url_for
from app.forms.financesForm import FinancesForm
from flask import session
from app.services.opeaiApiService import openaiApi
from app.services.financeService.FinanceService import FinanceService
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository

financeBp = Blueprint('finance', __name__, template_folder='templates/finances')

@financeBp.route('/finance', methods=['GET','POST'])
def finance():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    conexao = Conexao(Config(),'Financia')
    connRepository = ConexaoRepository(conexao) 
    finanService = FinanceService(connRepository)
    if request.method == 'POST':
        
        return redirect(url_for('finance.finance'))
    
    form = FinancesForm()
    try:
        despesas = finanService.exibirFinancas(session.get('usuario'))
        return render_template('finances/financas.html', form = form, finanService = despesas)
    except:
        
        return render_template('finances/financas.html', form = form)
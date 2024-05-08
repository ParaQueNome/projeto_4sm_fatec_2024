from flask import Blueprint, request
from flask import render_template, redirect
from config import Config
from flask import url_for
from app.forms.financesForm import FinancesForm
from flask import session
from app.services.opeaiApiService.openaiApi import OpenAiClient
from app.services.financeService.FinanceService import FinanceService
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository

financeBp = Blueprint('finance', __name__, template_folder='templates/finances')

@financeBp.route('/finance', methods=['GET','POST'])
def finance():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    form = FinancesForm()
    conexao = Conexao(Config(),'Financia')
    connRepository = ConexaoRepository(conexao) 
    finanService = FinanceService(connRepository)
    try:
        despesas = finanService.exibirFinancas(session.get('email'))
        print(despesas)
        #api = OpenAiClient()
        #answer = api.userFinances(1500, **despesas)
        return render_template('finances/financas.html', form = form,finanService = despesas) #, #answer = answer)
    except:
        return render_template('finances/financas.html', form = form)
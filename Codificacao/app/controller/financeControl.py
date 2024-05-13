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
    if request.method == 'POST':
        print(form.data)
        data_receitas = {'renda': form.data['renda']}
        finanService.inserirReceitas(session.get('email'), data_receitas)
        data_gastos = {'nome_gasto':form.data['nome_gasto'], 'valor': form.data['valor']}
        finanService.inserirGastos(session.get('email'), data_gastos)
        return redirect(url_for('finance.finance'))
    else:
        try:
            finan_data = finanService.exibirFinancas(session.get('email'))
            print(finan_data)
            #api = OpenAiClient()
            #answer = api.userFinances(1500, **despesas)
            return render_template('finances/financas.html', form = form, finanService = finan_data) #, #answer = answer)
        except:
            return render_template('finances/financas.html', form = form)
    
@financeBp.route('/despesas', methods=['POST'])
def despesas():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    form = FinancesForm()
    conexao = Conexao(Config(),'Financia')
    connRepository = ConexaoRepository(conexao)
    financService = FinanceService(connRepository)
    data_gastos = {'nome_gasto':form.data['nome_gasto'], 'valor': form.data['valor']}
    if request.method == 'POST':
        financService.inserirGastos(session.get('email'), data_gastos)
        return redirect(url_for('finance.finance'))

@financeBp.route('/receitas', methods=['POST'])
def receitas():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    form = FinancesForm()
    conexao = Conexao(Config(), 'Financia')
    connRepository = ConexaoRepository(conexao)
    financService = FinanceService(connRepository)
    data_receitas = {'renda': form.data['renda']}
    if request.method == 'POST':
        financService.inserirReceitas(session.get('email'), data_receitas)
        return redirect(url_for('finance.finance'))
    
@financeBp.route('/delete_receita', methods=['POST'])
def deleteReceita():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    conexao = Conexao(Config(), 'Financia')
    connRepository = ConexaoRepository(conexao)
    financService = FinanceService(connRepository)
    if request.method == 'POST':
        print(request.form['receita_id'])
        financService.deletarReceita(session.get('email'), request.form['receita_id'])
        return redirect(url_for('finance.finance'))

@financeBp.route('/delete_gasto', methods=['POST'])
def deleteDespesa():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    conexao = Conexao(Config(), 'Financia')
    connRepository = ConexaoRepository(conexao)
    financService = FinanceService(connRepository)
    if request.method == 'POST':
        print(request.form['gasto_id'])
        financService.deletarDespesa(session.get('email'), request.form['gasto_id'])
        return redirect(url_for('finance.finance'))

@financeBp.route('/update_gasto', methods=['POST'])
def updateDespesas():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    form = FinancesForm()
    gasto_id = request.form['gasto_id']
    nome_gasto = request.form['nomeGasto']
    valor_gasto = request.form['valorGasto']
    
    conexao = Conexao(Config(), 'Financia')
    connRepository = ConexaoRepository(conexao)
    financService = FinanceService(connRepository)
    
    financService.updateDespesas(session.get('email'), gasto_id, **form.data)
    
    return redirect(url_for('finance.finance'))


        



    

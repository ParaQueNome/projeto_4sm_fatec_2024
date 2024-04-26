from flask import Blueprint
from flask import render_template, redirect
from config import Config
from app.forms.authForm import AuthenticationForm
from app.forms.loginForm import LoginForm
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository
from app.services.authenticationService.signup import SignUp
from app.services.cryptographyService.cryptographyService import CryptographyService
from app.services.cryptographyService.cryptography import Cryptography
from app.services.authenticationService.login import Login
from flask import url_for
from app.services.authenticationService.session import SessionManager
from flask import session
from app.services.opeaiApiService.openaiApi import OpenAiClient


auth_bp = Blueprint('auth', __name__, template_folder='templates/auth')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    form = AuthenticationForm()
    if form.validate_on_submit():
        data = form.data
        conexao = Conexao(Config(),"Financia")
        conexaoRepository = ConexaoRepository(conexao)
        crypto = CryptographyService(Cryptography())
        signup = SignUp(conexaoRepository, crypto)
        if(signup.signup(data)):
            return 'cadastrado com sucesso'
    return render_template('auth/cadastro.html', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        conexao = Conexao(Config(), "Financia")
        conexaoRepository = ConexaoRepository(conexao)
        crypto = CryptographyService(Cryptography())
        login = Login(conexaoRepository, crypto)
        
        
        if(login.signIn(data)):
            return redirect(url_for('auth.cadastro'))
    #chat = OpenAiClient()
    #anwer = chat.userFinances(1500, **{'energia': 100, 'agua': 50, 'luz': 50, 'netflix': 25, 'faculdade':1200}) 
    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    SessionManager().close_session()
    return redirect(url_for('auth.login'))

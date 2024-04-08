from flask import Blueprint
from flask import render_template
from config import Config
from app.forms.auth import AuthenticationForm
from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository
from app.services.authenticationService.signup import SignUp
from app.services.cryptographyService.cryptographyService import CryptographyService
from app.services.cryptographyService.cryptography import Cryptography

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
    return 'login'  
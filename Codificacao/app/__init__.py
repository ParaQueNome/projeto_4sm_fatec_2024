from flask import Flask
from config import Config
from app.models.Conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository
from .services.Login import SignUp
from app.controller.auth import auth_bp






def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__)

    # Importando as rotas da aplicação
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Configurações opcionais da aplicação
   
    

    

    
    
    
    return app



from flask import Flask
from config import Config
from .models.conexao_mongo import Conexao




def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__)

    # Importando as rotas da aplicação
    #from app.auth import routes

    # Configurações opcionais da aplicação
    conexao = Config()
    bd = Conexao(conexao,"teste")
    data = {"nome": "guilherme"}
    bd.insert("test", **data)
    

    

    
    
    
    return app



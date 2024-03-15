from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config



def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__)

    # Importando as rotas da aplicação
    #from app.auth import routes

    # Configurações opcionais da aplicação
    app.config.from_object(Config)

    return app
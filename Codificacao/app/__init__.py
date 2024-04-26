from flask import Flask
from flask_login import LoginManager
from app.controller.authControl import auth_bp
from app.controller.financeControl import financeBp
from app.services.opeaiApiService.openaiApi import OpenAiClient

def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__, template_folder='templates')

    # Importando as rotas da aplicação
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(financeBp, url_prefix='/finance')

    # Configurações opcionais da aplicação
    app.config['SECRET_KEY'] = 't%23s342%%@'
    
    return app



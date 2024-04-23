from flask import Flask
from app.controller.authControl import auth_bp
from app.services.opeaiApi.openaiApi import OpenAiClient

def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__, template_folder='templates')

    # Importando as rotas da aplicação
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Configurações opcionais da aplicação
    app.config['SECRET_KEY'] = 't%23s342%%@'
    chat = OpenAiClient()
    chat.get_response()
   
    return app



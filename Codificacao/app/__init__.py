from flask import Flask
from flask_bootstrap import Bootstrap5
from app.controller.authControl import auth_bp
from app.controller.financeControl import financeBp
from app.controller.investmentControl import investmentBp
from app.controller.homepageControl import indexBp
from flask_wtf.csrf import CSRFProtect
from app.services.financeService.RedeNeuralService import RedeNeuralService

def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__, template_folder='templates')
    bootstrap = Bootstrap5(app)
    model = RedeNeuralService()
    #dados = {'c': 10, 'o': 5, 'h': 5, 'l': 10, 'v': 10}
    dados = [[25.13,25.16,25.23,25.13,20]]
    result = model.preview(dados)
    print(result)
    # Importando as rotas da aplicação
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(financeBp, url_prefix='/finance')
    app.register_blueprint(investmentBp, url_prefix='/trade')
    app.register_blueprint(indexBp, url_prefix='')
    # Configurações opcionais da aplicação
    app.config['SECRET_KEY'] = 't%23s342%%@'
    csrf = CSRFProtect(app)
    return app

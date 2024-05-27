from flask import Flask
from flask_bootstrap import Bootstrap5
from app.controller.authControl import auth_bp
from app.controller.financeControl import financeBp
from app.controller.investmentControl import investmentBp
from flask_wtf.csrf import CSRFProtect
from app.services.financeService.PolygonApiService import PolygonApiService

def create_app():
    # Criando instancia da aplicação Flask com o nome da aplicação
    app = Flask(__name__, template_folder='templates')
    bootstrap = Bootstrap5(app)
    ticker = PolygonApiService().carregarAcoes()
    print(ticker)
    for i in ticker:
        print(i)
    # Importando as rotas da aplicação
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(financeBp, url_prefix='/finance')
    app.register_blueprint(investmentBp, url_prefix='/trade')
    # Configurações opcionais da aplicação
    app.config['SECRET_KEY'] = 't%23s342%%@'
    csrf = CSRFProtect(app)
    return app

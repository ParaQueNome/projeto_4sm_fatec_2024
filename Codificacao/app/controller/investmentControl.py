from flask import Blueprint, request
from flask import render_template, redirect
from config import Config
from flask import url_for
from flask import session
from app.services.opeaiApiService.openaiApi import OpenAiClient
from app.services.financeService.PolygonApiService import PolygonApiService

investmentBp = Blueprint('trade', __name__, template_folder='templates/trades')

@investmentBp.route('/investment', methods=['GET','POST'])
def investment():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    
    
    return render_template('trades/trade.html')


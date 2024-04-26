from flask import Blueprint, request
from flask import render_template, redirect
from flask_login import login_required
from config import Config
from flask import url_for
from app.forms.financesForm import FinancesForm
from flask import session

financeBp = Blueprint('finance', __name__, template_folder='templates/finances')

@financeBp.route('/finance', methods=['GET','POST'])

def finance():
    if not session.get('usuario'):
        return redirect(url_for('auth.login'))
    if request.method == 'POST':
        return redirect(url_for('finance.finance'))
    
    form = FinancesForm()
    return render_template('finances/financas.html', form = form)
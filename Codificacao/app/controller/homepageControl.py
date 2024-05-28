from flask import Blueprint
from flask import render_template

indexBp = Blueprint('index', __name__, template_folder='templates/home')

@indexBp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home/index.html')

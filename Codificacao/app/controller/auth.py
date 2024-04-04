

from flask import Blueprint
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/cadastro', methods=['GET, POST'])
def cadastro():
    return 'cadastro'
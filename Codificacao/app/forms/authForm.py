from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms import PasswordField
from app.models.conexao_mongo import Conexao
from config import Config
from app.repositories.ConexaoRepository import ConexaoRepository

import re

class AuthenticationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        if len(username.data) < 4 and not username.data.isdigit():
            raise ValidationError('Nome de usuário deve conter pelo menos 4 caracteres e não pode ser apenas números.')

    def validate_password(self, password):
        if len(password.data) < 8 or not re.search(r'[!@#$%^&*(),.?":{}|<>]', password.data):
            raise ValidationError('Senha deve ter pelo menos 8 caracteres e conter pelo menos um caractere especial.')

    def validate_email(self, email):
        conexao = Conexao(Config(),"Financia")
        conexaoRepository = ConexaoRepository(conexao)
        data = {"email": email.data}
        conexaoRepository.select("usuario", **data)
        if(conexaoRepository):
            raise ValidationError('Email já cadastrado')
        if not re.search(r'@', email.data):
            raise ValidationError('Email deve conter "@".')
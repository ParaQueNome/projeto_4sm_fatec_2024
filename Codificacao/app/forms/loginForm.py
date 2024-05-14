from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms import SubmitField
from wtforms.validators import DataRequired, Length, Email
from wtforms import PasswordField

from app.models.conexao_mongo import Conexao
from app.repositories.ConexaoRepository import ConexaoRepository
from app.services.authenticationService.login import Login
from app.services.cryptographyService.cryptography import Cryptography
from app.services.cryptographyService.cryptographyService import CryptographyService
from config import Config

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField('Login')


    def validate_email(self, email):
        if email.data == '':
            raise ValidationError('Email não pode ser vazio')
        if email.data.find('@') == -1:
            raise ValidationError('Email deve conter @')
        if email.data.find('.') == -1:
            raise ValidationError('Email deve conter .')
        return email
        
    def validate_password(self, password):
        if password.data == '':
            raise ValidationError('Senha não pode ser vazia')
        if len(password.data) < 8:
            raise ValidationError('Senha deve ter no minimo 8 caracteres')
        data = {'password': password.data, 'email': self.email.data}
        conexao = Conexao(Config(), "Financia")
        conexaoRepository = ConexaoRepository(conexao)
        crypto = CryptographyService(Cryptography())
        login = Login(conexaoRepository, crypto)
        if not login.signIn(data):
            raise ValidationError('Senha incorreta')
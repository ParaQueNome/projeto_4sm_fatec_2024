from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms import PasswordField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()], render_kw={"placeholder:" "Seu endereço de email"})
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


    def validate_email(self, email):
        if email.data == '':
            raise ValidationError('Email não pode ser vazio')
        if email.data.find('@') == -1:
            raise ValidationError('Email deve conter @')
        if email.data.find('.') == -1:
            raise ValidationError('Email deve conter .')
        
    def validate_password(self, password):
        if password.data == '':
            raise ValidationError('Senha não pode ser vazia')
        if len(password.data) < 8:
            raise ValidationError('Senha deve ter no minimo 8 caracteres')
from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms import PasswordField

class FinancesForm(FlaskForm):
    
    renda = StringField('Renda', validators=[DataRequired()], render_kw={"placeholder": "Sua renda aqui"})
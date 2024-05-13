from flask_wtf import FlaskForm
from wtforms import StringField, ValidationError, HiddenField
from wtforms.validators import DataRequired

class FinancesForm(FlaskForm):
    nome_receita = StringField('Nome Renda', validators=[DataRequired()], render_kw={"placeholder": "Nome da renda"})
    renda = StringField('Renda', validators=[DataRequired()], render_kw={"placeholder": "Sua renda aqui"})
    nome_gasto = StringField('Nome do gasto', validators=[DataRequired()], render_kw={"placeholder": "Nome do gasto"})
    valor = StringField('Valor', validators=[DataRequired()], render_kw={"placeholder": "Valor da despesa"})

    def validate_renda(self, renda):
        if renda.data == "":
            raise ValidationError("Renda não pode ser vazia")
        return renda
    
    def validate_nome_gasto(self, nome_gasto):
        if nome_gasto.data == "":
            raise ValidationError("Nome do gasto não pode ser vazio")
        return nome_gasto
    
    def validate_valor(self, valor):
        if valor.data == "":
            raise ValidationError("Valor não pode ser vazio")
        return valor
from sys import flags
from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class YeastsForm(FlaskForm):
    yeasts_name = StringField('Сорт дрожжей', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
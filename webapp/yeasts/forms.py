from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from webapp.yeasts.enums import Type_of_yeast
from wtforms.validators import DataRequired

class YeastsForm(FlaskForm):
    yeasts_name = SelectField(
        'Сорт дрожжей:',
        choices=Type_of_yeast.list_names(),
        render_kw={'class': 'form-select'}
        )
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})
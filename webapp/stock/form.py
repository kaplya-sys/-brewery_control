from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, FloatField, StringField
from wtforms.validators import DataRequired

from webapp.db import db
from webapp.stock.enums import ProductType


class AppendProductForm(FlaskForm):
    
    name_product0 = StringField('Наименование', validators=[DataRequired()], render_kw={"class": "form-control"})
    type_product0 = SelectField('Тип сырья', validate_choice=[DataRequired()], render_kw={"class": "form-control"})
    amount_product0 = FloatField('Колличество сырья', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    def __init__(self, *args, **kwargs):
        super(AppendProductForm, self).__init__( *args, **kwargs)
        self.type_product0.choices = [(prod.value, ProductType.type_name(prod)) for prod in ProductType]
        self.type_product0.choices.insert(0, (None, '--------'))

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired

from webapp.db import db
from webapp.tank.enums import TitleBeer
from webapp.tank.models import Tank


class CreateTankForm(FlaskForm):

    number = IntegerField('Номер ЦКТ', validators=[DataRequired()],render_kw={"class": "form-control"})
    title = SelectField('Названте сорта',
         validate_choice=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})

    def __init__(self, *args, **kwargs):
        super(CreateTankForm, self).__init__(*args, **kwargs)
        self.title.choices = [(i.value, TitleBeer.product_name(i)) for i in TitleBeer]

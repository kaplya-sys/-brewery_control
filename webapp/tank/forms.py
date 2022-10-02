from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField, SubmitField, SelectField, IntegerField, BooleanField
from wtforms.validators import DataRequired, EqualTo

from webapp.tank.enums import TitleBeer


class CreateTankForm(FlaskForm):
    number = IntegerField('Номер ЦКТ',render_kw={"class": "form-control"})
    title = SelectField('Названте сорта', choices=[
        (TitleBeer.kellerbier.value, 'Kellerbier'),
        (TitleBeer.dunkelbier.value, 'Dunkelbier'),
        (TitleBeer.bropils.value, 'Bro Pils'),
        (TitleBeer.wheatbeer.value, 'Пшеничное'),
        (TitleBeer.traditional_dark.value, 'Традиционное Темное'),
        (TitleBeer.traditional_light.value, 'Традиционное Светлое'), 
        (TitleBeer.traditional_wheat.value, 'Традиционное Пшеничное'),
        (TitleBeer.cider.value, 'Пивной напиток'),
    ], render_kw={"class": "form-control"})
    yeast = StringField('Дрожжи', render_kw={"class": "form-control"})
    expected_volume = IntegerField('Объём', render_kw={"class": "form-control"})
    actual_volume = IntegerField('Объём', render_kw={"class": "form-control"})
    beer_grooving = BooleanField('Шпунт', default=False, render_kw={"class": "form-control"})
    cooling = BooleanField('Охлаждение', default=False, render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})

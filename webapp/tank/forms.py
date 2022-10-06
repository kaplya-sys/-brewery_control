from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, BooleanField, FloatField, HiddenField
from wtforms.validators import DataRequired, EqualTo

from webapp.db import db
from webapp.tank.enums import TitleBeer
from webapp.tank.models import Tank


class CreateTankForm(FlaskForm):
    number = IntegerField('Номер ЦКТ', validators=[DataRequired()],render_kw={"class": "form-control"})
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


class MeasuringForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(MeasuringForm, self).__init__(*args, **kwargs)
        self.tank_id.choices = [(i.id, i) for i in Tank.query.all()]

    tank_id = SelectField('Номер ЦКТ',validators=[DataRequired()], render_kw={"class": "form-control"})
    temperature = FloatField('Температура', validators=[DataRequired()], render_kw={"class": "form-control"})
    density = FloatField('Плотность', validators=[DataRequired()], render_kw={"class": "form-control"})
    pressure = FloatField('Давление', validators=[DataRequired()], render_kw={"class": "form-control"})
    comment = StringField('Комментарии', render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})

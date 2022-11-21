from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    IntegerField,
    FloatField
)
from wtforms.validators import DataRequired

from webapp.tank.enums import TitleBeer
from webapp.tank.utils import generate_title_beer_list


class CreateTankForm(FlaskForm):
    number = IntegerField(
        'Номер ЦКТ',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    title = SelectField(
        'Сорт пива',
        validate_choice=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    yeasts = SelectField(
        'Дрожжи',
        validate_choice=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Добавить',
        render_kw={"class": "btn btn-primary"}
    )

    def __init__(self, *args, **kwargs):
        super(CreateTankForm, self).__init__(*args, **kwargs)
        self.title.choices = [
            (i.value, TitleBeer.product_name(i)) for i in TitleBeer
        ]
        self.title.choices.insert(0, (None, 'Выберите сорт'))


class MeasuringForm(FlaskForm):
    tank_id = SelectField(
        'Номер ЦКТ',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    temperature = FloatField(
        'Температура',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    density = FloatField(
        'Плотность',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    pressure = FloatField(
        'Давление',
        default=0,
        render_kw={"class": "form-control"}
    )
    comment = StringField(
        'Комментарии',
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Добавить',
        render_kw={"class": "btn btn-primary"}
    )

    def __init__(self, *args, **kwargs):
        super(MeasuringForm, self).__init__(*args, **kwargs)
        self.tank_id.choices = generate_title_beer_list()


class PourBeerForm(FlaskForm):
    tank_id = SelectField(
        'Номер ЦКТ',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    volume = IntegerField(
        'Объём кеги',
        validators=[DataRequired()],
        default=30,
        render_kw={"class": "form-control"}
    )
    kegs = IntegerField(
        'Количество кег',
        validators=[DataRequired()],
        render_kw={"class": "form-control"}
    )
    submit = SubmitField(
        'Разлить',
        render_kw={"class": "btn btn-primary"}
    )

    def __init__(self, *args, **kwargs):
        super(PourBeerForm, self).__init__(*args, **kwargs)
        self.tank_id.choices = generate_title_beer_list()

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

from webapp.tank.enums import TitleBeer


class CreateTankForm(FlaskForm):
    number = IntegerField('Номер ЦКТ', validators=[DataRequired()],render_kw={"class": "form-control"})
    title = SelectField('Названте сорта', choices=[
        (getattr(TitleBeer, enum.variable_name).value, TitleBeer.product_name(enum))for enum in TitleBeer],
         validate_choice=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})

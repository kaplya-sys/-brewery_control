from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, IntegerField
from wtforms.validators import DataRequired

from webapp.tank.enums import TitleBeer


class CreateTankForm(FlaskForm):

    def __init__(self, *args, **kwargs):
        super(CreateTankForm, self).__init__(*args, **kwargs)
        self.title.choices = [(i.value, TitleBeer.product_name(i)) for i in TitleBeer]

    number = IntegerField('Номер ЦКТ', validators=[DataRequired()],render_kw={"class": "form-control"})
    title = SelectField('Названте сорта',
         validate_choice=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})

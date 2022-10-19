from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from webapp.yeasts.enums import TypeOfYeast


class YeastsForm(FlaskForm):
    yeasts_name = SelectField('Сорт дрожжей:', render_kw={'class': 'form-select'})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})

    def __init__(self, *args, **kwargs):
        super(YeastsForm, self).__init__(*args, **kwargs)
        self.yeasts_name.choices = [(key.name, key.value) for key in TypeOfYeast]

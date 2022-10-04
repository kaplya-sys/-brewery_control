from flask_wtf import FlaskForm
from webapp.user.enums import Profession
from wtforms import PasswordField, StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, EqualTo

class CreateUserForm(FlaskForm):
    username = StringField(
        'Имя пользователя:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    firstname = StringField(
        'Имя:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    lastname = StringField(
        'Фамилия:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    password = PasswordField(
        'Пароль:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    re_password = PasswordField(
        'Повторите пароль:',
        validators=[
            DataRequired(),
            EqualTo(password)
            ],
        render_kw={'class': 'form-control'}
        )
    position = SelectField(
        'Должность:',
        choices=[
            (Profession.brewer.value, Profession.brewer.get_translated_value()),
            (Profession.assistant.value, Profession.assistant.get_translated_value())
            ],
        render_kw={'class': 'form-select'}
        )
    submit = SubmitField(
        'Отправить',
        render_kw={'class': 'btn btn-primary'}
        )
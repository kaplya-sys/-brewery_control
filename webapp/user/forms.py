from flask_wtf import FlaskForm
from webapp.user.enums import Profession
from wtforms import StringField, PasswordField, SubmitField, SelectField
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
            (Profession.brewer.value, 'Пивовар'),
            (Profession.assistant.value, 'Помощник')
            ],
        render_kw={'class': 'form-select'}
        )
    submit = SubmitField(
        'Отправить',
        render_kw={'class': 'btn btn-primary'}
        )
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField(
        'Имя пользователя:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    password = PasswordField(
        'Пароль:',
        validators=[DataRequired()],
        render_kw={'class': 'form-control'}
        )
    remember_me = BooleanField(
        'Запомнить меня',
        render_kw={'class': 'form-check-input'}
        )
    submit = SubmitField(
        'Войти',
        render_kw={'class': 'btn btn-success'}
        )
    
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
            ('Пивовар', 'пивовар'),
            ('Помощник', 'помощник')
            ],
        render_kw={'class': 'form-select'}
        )
    submit = SubmitField(
        'Отправить',
        render_kw={'class': 'btn btn-primary'}
        )
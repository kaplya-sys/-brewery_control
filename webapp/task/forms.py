from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, StringField, TextAreaField
from wtforms.validators import DataRequired
from webapp.user.models import User
from webapp.user.enums import Profession


class CreateTasksForm(FlaskForm):

    title = StringField('Заголовок:', validators=[DataRequired()],render_kw={"class": "form-control"})
    text = TextAreaField('Текст:', validators=[DataRequired()], render_kw={"class": "form-control"})
    user = SelectField('Выберите сотрудника: ', render_kw={'class': 'form-select'})
    submit = SubmitField('Добавить', render_kw={"class": "btn btn-primary"})


    def __init__(self, *args, **kwargs):
        super(CreateTasksForm, self).__init__(*args, **kwargs)
        self.user.choices = [
            (user.id, f"{user.firstname} {user.lastname}") for user in User.query.filter(
                User.employee_position == Profession.assistant
                ).all()]
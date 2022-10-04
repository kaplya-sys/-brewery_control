from getpass import getpass
from webapp.user.enums import Profession
import sys

from webapp import create_app
from webapp.db import db
from webapp.user.models import User

app = create_app()
with app.app_context():
    username = input('ВВедите имя пользователя: ')

    if User.query.filter(User.username == username).count():
        print('Пользователь с таким именем существует.')
        sys.exit(0)

    password = getpass('Введите пароль: ')
    confirm_password = getpass('Повторите пароль: ')

    if password != confirm_password:
        print('Пароли не совпадают.')
        sys.exit(0)

    new_user = User(username=username, employee_position=Profession.admin)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    print('Пользователь успешно добавлен.')

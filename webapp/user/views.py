from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user
from webapp.db import db
from webapp.user.forms import LoginForm, CreateUserForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__)

@blueprint.route('/')                                   #
def index():                                            # тестовый адрес
    return render_template('index.html', title='test')  #

@blueprint.route('/auth/log-in')
def log_in():
    if current_user.is_authenticated:
        return redirect(url_for('user.index')) # необходимо добавить главную страницу
        
    page_title = 'Авторизация'
    login_form = LoginForm()
    
    return render_template('login.html', title=page_title, form=login_form)
    
@blueprint.route('/create/new-user')
def create_user():      
    page_title = 'Регистрация нового пользователя'
    create_form = CreateUserForm()
    
    return render_template('create_user.html', title=page_title, form=create_form)
    
@blueprint.route('/auth/process-log-in', methods=['POST'])
def process_log_in():
    form = LoginForm()

    if form.validate_on_submit:
        user = User.query.filter(User.username == form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Вы успешно авторизовались.')

            return redirect(url_for('user.index')) # необходимо добавить главную страницу           
        flash('Неправильный имя пользователя или пароль.')

        return redirect(url_for('user.log_in'))
        
@blueprint.route('/create/process-create-user', methods=['POST'])
def process_create_user():
    form = CreateUserForm()

    if form.validate_on_submit:
        if User.query.filter(User.username == form.username.data).count():
            flash('Пользователь с таким именем существует.')

            return redirect(url_for('user.create_user'))

        new_user = User(
            username=form.username.data,
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            employee_position=form.position.data
            )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Пользователь успешно зарегистрирован.')

        return redirect(url_for('user.create_user'))

@blueprint.route('/logout')
def logout():
    logout_user()

    return redirect(url_for('user.log_in'))        
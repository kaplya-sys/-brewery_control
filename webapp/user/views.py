from flask import Blueprint, flash, render_template, redirect, url_for
from webapp.db import db
from webapp.user.forms import  CreateUserForm
from webapp.user.models import User

blueprint = Blueprint('user', __name__)
    
@blueprint.route('/create/new-user')
def create_user():      
    page_title = 'Регистрация нового пользователя'
    create_form = CreateUserForm()
    
    return render_template('create_user.html', title=page_title, form=create_form)             
        
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
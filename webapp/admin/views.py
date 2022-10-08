from flask import Blueprint, flash, render_template, redirect, url_for
from webapp.admin.forms import  CreateUserForm
from webapp.db import db
from webapp.user.decorators import superuser_required
from webapp.user.models import User

blueprint = Blueprint('admin', __name__, url_prefix='/admin')
    
@blueprint.route('/create/new-user')
@superuser_required
def create_user():  
    page_title = 'Регистрация нового пользователя'
    create_form = CreateUserForm()
    
    return render_template('admin/create_user.html', title=page_title, form=create_form)             
        
@blueprint.route('/create/process-create-user', methods=['POST'])
@superuser_required
def process_create_user():
    form = CreateUserForm()
  
    if form.validate_on_submit:
        if User.query.filter(User.username == form.username.data).count():
            flash('Пользователь с таким именем существует.')

            return redirect(url_for('admin.create_user'))

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

        return redirect(url_for('admin.create_user'))
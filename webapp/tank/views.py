from sqlalchemy import exc
from flask import Blueprint ,flash, render_template, redirect, url_for

from webapp.db import db
from webapp.tank.forms import CreateTankForm
from webapp.tank.models import Tank, Measuring

blueprint = Blueprint('tank', __name__, url_prefix='/tank')

@blueprint.route('/create-tank')
def create_tank():
    page_title = 'Добавить ЦКТ'
    create_form = CreateTankForm()

    return render_template('tank/create_tank.html', title=page_title, form=create_form)

@blueprint.route('/process-create_tank', methods=['POST'])
def process_create_tank():
    form = CreateTankForm()

    if form.validate_on_submit:
            new_tank = Tank(
            number=form.number.data,
            title=form.title.data,
            yeast=form.yeast.data
            )
            try:
                db.session.add(new_tank)
                db.session.commit()
                flash('ЦКТ добавлен')
            except exc.IntegrityError:
                db.session().rollback()
                flash('Данный ЦКТ уже занят')
                return redirect(url_for('tank.create_tank'))

    return render_template('base.html', title='add tank')

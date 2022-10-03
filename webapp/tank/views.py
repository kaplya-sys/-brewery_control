from datetime import datetime
from sqlalchemy import exc
from flask import Blueprint ,flash, render_template, redirect, url_for

from webapp.db import db
from webapp.tank.forms import CreateTankForm, MeasuringForm
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


@blueprint.route('/measuring')
def measuring_tank():
    page_title = 'Внести измерения'
    create_form = MeasuringForm()

    return render_template('tank/measuting.html', title=page_title, form=create_form)


@blueprint.route('/process-measuring', methods=['POST'])
def process_measuring():
    form = MeasuringForm()

    if form.validate_on_submit():
        new_measuring = Measuring(
            temperature = form.temperature.data,
            density = form.density.data,
            pressure = form.pressure.data,
            # create_at = datetime.now(),
            comment = form.comment.data,
            tank_id = form.tank_id.data
        )
        db.session.add(new_measuring)
        db.session.commit()
        flash('Данные успешно заполнены')
        return redirect(url_for('tank.measuring_tank'))
    
    flash('Что-то пошло не так')
    return redirect(url_for('tank.measuring_tank'))

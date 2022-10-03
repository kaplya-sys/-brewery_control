from flask import Blueprint ,flash, render_template, redirect, url_for

from webapp.db import db
from webapp.tank.forms import CreateTankForm
from webapp.tank.models import Tank, Measuring
from webapp.user.decorators import brewer_required

blueprint = Blueprint('tank', __name__, url_prefix='/tank')

@blueprint.route('/create-tank')
@brewer_required
def create_tank():
    page_title = 'Добавить ЦКТ'
    create_form = CreateTankForm()

    return render_template('tank/create_tank.html', title=page_title, form=create_form)

@blueprint.route('/process-create_tank', methods=['POST'])
@brewer_required
def process_create_tank():
    form = CreateTankForm()

    if form.validate_on_submit:
        if Tank.query.filter(Tank.number == form.number.data).count():
            flash('Данный ЦКТ уже занят')
            return redirect(url_for('tank.create_tank'))

        new_tank = Tank(
            number=form.number.data,
            title=form.title.data,
            )   
        db.session.add(new_tank)
        db.session.commit()
        flash('ЦКТ добавлен')

    return render_template('base.html', title='add tank')

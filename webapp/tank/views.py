from unicodedata import name
from flask import Blueprint ,flash, render_template, redirect, url_for, request
from flask_login import login_required

from webapp.db import db
from webapp.tank.forms import CreateTankForm, MeasuringForm
from webapp.tank.models import Tank, Measuring
from webapp.tank.utils import (
    number_of_brews_for_full_tank,
    planned_expected_volume,
    is_beer_need_cooling,
    is_beer_need_grooving,
    create_diagrams_for_tanks
    )
from webapp.yeasts.models import Yeasts
from webapp.yeasts.utils import get_need_yeasts, get_list_of_suitable_tanks
from webapp.user.decorators import brewer_required

blueprint = Blueprint('tank', __name__, url_prefix='/tank')


@blueprint.route('/')
@login_required
def view_tanks():
    diagrams = create_diagrams_for_tanks()
    page_title = 'Активные ЦКТ'
  
    return render_template('tank/tanks_view.html', title=page_title, diagrams=diagrams)

@blueprint.route('/<int:tank_id>')
@login_required
def view_tank_info(tank_id):
    tank = Tank.query.filter(Tank.id == tank_id).first()
    yeats = Yeasts.query.filter(Yeasts.id == tank.yeasts_id).first()
    measuring = Measuring.query.order_by(Measuring.create_at.asc()).filter(Measuring.tank_id == tank_id).all()
    page_title = 'Информация по ЦКТ'
    
    return render_template('tank/tank_info.html', title=page_title, tank=tank, measuring=measuring, yeats=yeats)


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
        if not Tank.query.count():
            previous_brew_number = 0
        else:
            previous_brew_number = Tank.query.order_by(Tank.id.desc()).first().brew_number_last
        numbers_brew = number_of_brews_for_full_tank(form.number.data)

        new_tank = Tank(
            number=form.number.data,
            title=form.title.data,
            expected_volume= numbers_brew * planned_expected_volume(form.number.data),
            brew_number_first = previous_brew_number + 1,
            brew_number_last = previous_brew_number + numbers_brew,
            )   
        db.session.add(new_tank)
        db.session.commit()
        flash('ЦКТ добавлен')

    return render_template('base.html', title='add tank')


@blueprint.route('/measuring')
def measuring_tank():
        page_title = 'Внести измерения'
        create_form = MeasuringForm()

        return render_template('tank/measuring.html', title=page_title, form=create_form)


@blueprint.route('/process-measuring', methods=['POST'])
def process_measuring():
    form = MeasuringForm()
    if form.validate_on_submit():
        new_measuring = Measuring(
            temperature = form.temperature.data,
            density = form.density.data,
            pressure = form.pressure.data,
            comment = form.comment.data,
            tank_id = form.tank_id.data
        )
        tank = Tank.query.get(new_measuring.tank_id)
        title_tank = tank.title
        if not tank.cooling:
            if not tank.beer_grooving:
                tank.beer_grooving = is_beer_need_grooving(title_tank, new_measuring.density)
            tank.cooling = is_beer_need_cooling(title_tank, new_measuring.density)
            
        db.session.add(new_measuring)
        db.session.commit()
        flash('Данные успешно заполнены')
        return redirect(url_for('tank.measuring_tank'))
    
    for field, error in form.errors.items():
        flash(f'{field} is {error[0]}')
    return redirect(url_for('tank.measuring_tank'))


@blueprint.route('/index', methods=['GET', 'POST'])
def get_choise_suitable_tanks():
    if request.method == 'POST':
        choise_title_beer = str(request.data)[2:-1]
        yeast = get_need_yeasts(choise_title_beer)
        list_tanks = get_list_of_suitable_tanks(yeast)
        if not list_tanks:
            new_yeast = Yeasts(
                name=yeast
            )
    return redirect(url_for('tank.create_tank'))

import json
from flask import (
    Blueprint,
    flash,
    render_template,
    redirect,
    url_for,
    request,
    jsonify
)
from flask_login import login_required

from webapp.db import db
from webapp.tank.forms import CreateTankForm, MeasuringForm, PourBeerForm
from webapp.tank.models import Tank, Measuring
from webapp.tank.utils import (
    create_diagrams_for_tanks,
    number_of_brews_for_full_tank,
    planned_expected_volume,
    is_beer_need_cooling,
    is_beer_need_grooving,
    show_error_message,
)
from webapp.yeasts.models import Yeasts
from webapp.yeasts.utils import (
    get_the_right_yeasts,
    get_list_of_suitable_tanks,
    get_id_now_yeast
)
from webapp.user.decorators import special_users_required

blueprint = Blueprint('tank', __name__, url_prefix='/tank')


@blueprint.route('/<int:tank_id>')
@login_required
def view_tank_info(tank_id):
    tank = Tank.query.filter(Tank.id == tank_id).first()
    yeats = Yeasts.query.filter(Yeasts.id == tank.yeasts_id).first()
    measuring = Measuring.query.order_by(
        Measuring.create_at.asc()
    ).filter(
        Measuring.tank_id == tank_id
    ).all()
    page_title = 'Информация по ЦКТ'
    return render_template(
        'tank/tank_info.html',
        title=page_title,
        tank=tank,
        measuring=measuring,
        yeats=yeats
    )


@blueprint.route('/create-tank')
@special_users_required
def create_tank():
    page_title = 'Добавление ЦКТ'
    create_form = CreateTankForm()
    return render_template(
        'tank/create_tank.html',
        title=page_title,
        form=create_form
    )


@blueprint.route('/process-create_tank', methods=['POST'])
@special_users_required
def process_create_tank():
    form = CreateTankForm()
    if form.validate_on_submit:
        if Tank.query.filter(Tank.number == form.number.data).count():
            flash('Данный ЦКТ уже занят')
            return redirect(url_for('tank.create_tank'))
        if not Tank.query.count():
            previous_brew_number = 0
        else:
            previous_brew_number = Tank.query.order_by(
                Tank.id.desc()
            ).first().brew_number_last
        numbers_brew = number_of_brews_for_full_tank(form.number.data)
        now_id, generation = get_id_now_yeast(form.yeasts.data)
        name_yeasts = get_the_right_yeasts(form.title.data)
        if now_id == -1:
            generation = 0
            flash('Нет подходящих дрожжей. Нужно использовать сухие')
        new_yeast = Yeasts(
            name=name_yeasts,
            cycles=generation + 1
        )
        db.session.add(new_yeast)
        db.session.commit()
        new_tank = Tank(
            number=form.number.data,
            title=form.title.data,
            yeasts_id=new_yeast.id,
            expected_volume=numbers_brew * planned_expected_volume(
                form.number.data
            ),
            brew_number_first=previous_brew_number + 1,
            brew_number_last=previous_brew_number + numbers_brew,
        )
        db.session.add(new_tank)
        db.session.commit()
        flash('ЦКТ добавлен')
    return redirect(url_for('tank.view_tank_info', tank_id=new_tank.id))


@blueprint.route('/measuring')
@login_required
def measuring_tank():
    page_title = 'Внесение измерения'
    create_form = MeasuringForm()
    return render_template(
        'tank/measuring.html',
        title=page_title,
        form=create_form
    )


@blueprint.route('/process-measuring', methods=['POST'])
@login_required
def process_measuring():
    form = MeasuringForm()
    if form.validate_on_submit():
        new_measuring = Measuring(
            temperature=form.temperature.data,
            density=form.density.data,
            pressure=form.pressure.data,
            comment=form.comment.data,
            tank_id=form.tank_id.data
        )
        tank = Tank.query.get(new_measuring.tank_id)
        title_tank = tank.title
        if not tank.cooling:
            if not tank.beer_grooving:
                tank.beer_grooving = is_beer_need_grooving(
                    title_tank,
                    new_measuring.density
                )
            tank.cooling = is_beer_need_cooling(
                title_tank,
                new_measuring.density
            )
        db.session.add(new_measuring)
        db.session.commit()
        flash('Данные успешно заполнены')
        return redirect(url_for('tank.measuring_tank'))
    show_error_message(form.errors.items())
    return redirect(url_for('tank.measuring_tank'))


@blueprint.route('/yeast-request-processing', methods=['GET', 'POST'])
@login_required
def get_choice_suitable_tanks():
    if request.method == 'POST':
        choice_title_beer = str(request.data)[2:-1]
        yeast = get_the_right_yeasts(choice_title_beer)
        list_tanks = get_list_of_suitable_tanks(yeast)
        if not list_tanks:
            return ['Нет подходящих дрожжей']
        else:
            jsonList = json.dumps(list_tanks)
            return jsonList
    return redirect(url_for('tank.create_tank'))


@blueprint.route('/pour-beer')
@login_required
def pour_beer():
    page_title = 'Разлив пива из ЦКТ'
    form = PourBeerForm()
    return render_template('tank/pour_beer.html', title=page_title, form=form)


@blueprint.route('/process-pour-beer', methods=['POST'])
@login_required
def process_pour_beer():
    form = PourBeerForm()
    if form.validate_on_submit():
        volume_of_bottled_beer = form.kegs.data * form.volume.data
        tank = Tank.query.filter(Tank.id == form.tank_id.data).first()
        if tank:
            tank.actual_volume += volume_of_bottled_beer
            db.session.commit()
            flash('Данные успешно внесены')
        else:
            flash('Выбранная ЦКТ не обнаружена.')
    else:
        show_error_message(form.errors.items())
    return redirect(url_for('tank.pour_beer'))


@blueprint.route('/tanks-view', methods=['GET'])
@login_required
def view_tanks():
    diagrams = create_diagrams_for_tanks()
    return jsonify({
        'diagrams': diagrams
    })


@blueprint.route('/tanks-info', methods=['GET'])
@login_required
def view_info():
    args = request.args
    tank_measuring = []
    tank = Tank.query.filter(Tank.id == args['tank_id']).first()
    yeats = Yeasts.query.filter(Yeasts.id == tank.yeasts_id).first()
    for measuring in Measuring.query.order_by(
        Measuring.create_at.asc()
    ).filter(
        Measuring.tank_id == tank.id
    ).all():
        tank_measuring.append(dict(
            temperature=measuring.temperature,
            density=measuring.density,
            pressure=measuring.pressure,
            comment=measuring.comment,
            create_at=measuring.create_at.strftime("%d-%m-%Y, %H:%M")
        ))
    return jsonify({
        'tank_number': tank.number,
        'tank_title_value': tank.title.value,
        'yeats': yeats.name.value,
        'tank_beer_grooving': 'Да' if tank.beer_grooving else 'Нет',
        'tank_cooling': 'Да' if tank.cooling else 'Нет',
        'tank_expected_volume': tank.expected_volume,
        'tank_actual_volume': tank.actual_volume,
        'measuring': tank_measuring
    })

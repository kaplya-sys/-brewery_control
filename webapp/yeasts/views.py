from flask import Blueprint, flash, render_template, redirect, url_for
from flask_login import login_required

from webapp.db import db
from webapp.yeasts.forms import YeastsForm
from webapp.yeasts.models import Yeasts

blueprint = Blueprint('yeasts', __name__, url_prefix='/components')

@blueprint.route('/add-yeasts')
@login_required
def add_yeasts():
    page_title = 'Дрожжи'
    yeasts_form = YeastsForm()

    return render_template('yeasts/index.html', title=page_title, form=yeasts_form)

@blueprint.route('/process-create-add-yeasts', methods=['POST'])
@login_required
def process_create_add_yeasts():
    form = YeastsForm()

    if form.validate_on_submit:
        yeasts = Yeasts.query.filter(Yeasts.name == form.yeasts_name.data).first()

        if yeasts:
            if yeasts.cycles >= 6:
                flash('Превышен лимит использования дрожжей')
                db.session.delete(yeasts)
                db.session.commit()
                return redirect(url_for('yeasts.add_yeasts'))
            else:
                yeasts.cycles+=1
                db.session.commit()
                flash('Дрожжи успешно обновлены.')
                return redirect(url_for('yeasts.add_yeasts'))

        new_yeasts = Yeasts(name=form.yeasts_name.data, cycles=1)
        db.session.add(new_yeasts)
        db.session.commit()

        flash('Дрожжи успешно добавлены.')

        return redirect(url_for('yeasts.add_yeasts'))
    return redirect(url_for('yeasts.add_yeasts'))
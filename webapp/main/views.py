from flask import Blueprint, render_template
from flask_login import login_required

from webapp.tank.utils import (create_diagrams_for_tanks)

blueprint = Blueprint('main', __name__)


@blueprint.route('/')
@login_required
def view_tanks():
    diagrams = create_diagrams_for_tanks()
    page_title = 'Активные ЦКТ'
  
    return render_template('main/index.html', title=page_title, diagrams=diagrams)

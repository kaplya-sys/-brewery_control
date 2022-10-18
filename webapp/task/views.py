from datetime import datetime
from flask import Blueprint ,flash, jsonify, render_template, redirect, request, url_for

from webapp.user.decorators import brewer_required
from webapp.task.forms import CreateTasksForm
from webapp.task.models import Task
from webapp.db import db

blueprint = Blueprint('tasks', __name__, url_prefix='/task')

@blueprint.route('/')
@brewer_required
def view_tasks():
    page_title = 'Задачи'
    tasks = Task.query.all()
    
    return render_template('task/all_tasks.html', tasks=tasks, title=page_title)


@blueprint.route('/create')
@brewer_required
def task_create():
    page_title = 'Добавить задачу'
    form = CreateTasksForm()

    return render_template('task/create_task.html', form=form, title=page_title)

@blueprint.route('/process-create-task', methods=['POST'])
@brewer_required
def process_create_task():
    form = CreateTasksForm()
    new_task = Task(
        title=form.title.data,
        text=form.text.data,
        user_id=form.user.data
        )
    db.session.add(new_task)
    db.session.commit()
    flash('Задача успешно добавлена.')

    return redirect(url_for('tasks.task_create'))

@blueprint.route('/update-task/<int:task_id>', methods=['GET'])
@brewer_required
def update_task(task_id):

    task = Task.query.filter(Task.id==task_id).first()
    return jsonify({
        'id': task.id,
        'title': task.title,
        'text': task.text
    })

@blueprint.route('/process-update-task', methods=['POST'])
@brewer_required
def process_update_task():
    data = request.get_json()
    task = Task.query.filter(Task.id==data['id']).first()
    task.title = data['title']
    task.text = data['text']
    task.update_at = datetime.now()
    db.session.commit()
    flash('Задача успешно обновлена.')
    
    return redirect(url_for('tasks.view_tasks'))


@blueprint.route('/process-delete-task', methods=['POST'])
@brewer_required
def process_delete_task():
    data = request.form.getlist('task_checked')
    for id in data:
        Task.query.filter(Task.id==id).delete()
    db.session.commit()
    flash('Задача успешно удалена.')
    
    return redirect(url_for('tasks.view_tasks'))
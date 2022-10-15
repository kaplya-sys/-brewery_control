from functools import wraps
from flask import current_app, flash, request, redirect, url_for, render_template
from flask_login import config, current_user

def superuser_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if request.method in config.EXEMPT_METHODS:
            return func(*args, **kwargs)
        elif current_app.config.get('LOGIN_DISABLED'):
            return func(*args, **kwargs)
        elif not current_user.is_authenticated:
            return current_app.login_manager.unauthorized()
        elif not current_user.is_superuser:
            flash('Эта страница доступна только админам')
            return redirect(url_for('user.login'))
        return func(*args, **kwargs)
    
    return decorated_view

def brewer_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_brewer or current_user.is_superuser:
            return func(*args, **kwargs)
        else:
            flash('Нет прав для данного действия')
            return render_template('base.html', title='Нет прав для данного действия')
    return decorated_function
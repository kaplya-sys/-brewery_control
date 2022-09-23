from functools import wraps
from flask import current_app, flash, request, redirect, url_for
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
            return redirect(url_for('user.index'))  # необходимо добавить главную страницу  
        return func(*args, **kwargs)
    
    return decorated_view
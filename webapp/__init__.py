from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from webapp.db import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.tank.views import blueprint as tank_blueprint
from webapp.admin.views import blueprint as admin_blueprint
from webapp.yeasts.views import blueprint as yeasts_blueprint

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(yeasts_blueprint)
    app.register_blueprint(tank_blueprint)

    db.init_app(app)
    migrate = Migrate(app, db, compare_type = True)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
        
    return app
from enum import Enum
from webapp.db import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class Post(Enum):
    Пивовар = 1
    Помощник = 2

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), index=True, nullable=False, unique=True)
    firstname = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    password = db.Column(db.String(), nullable=False)
    employee_position = db.Column(db.Enum(Post), nullable=False)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
        
    @property
    def is_superuser(self):
        return self.employee_position == 'Пивовар'
    
    def __repr__(self):
        return f"User {self.id} {self.username}"
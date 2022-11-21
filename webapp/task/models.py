from sqlalchemy.orm import relationship
from datetime import datetime
from webapp.db import db


class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False,)
    text = db.Column(db.String, nullable=False)
    completed = db.Column(db.Boolean, default=False)
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    update_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = relationship('User', backref='tasks')

from webapp.db import db
from webapp.yeasts.enums import TypeOfYeast


class Yeasts(db.Model):
    __tablename__ = "yeasts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Enum(TypeOfYeast), nullable=False)
    cycles = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"Дрожжи {self.name.value} {self.cycles}-генерации"

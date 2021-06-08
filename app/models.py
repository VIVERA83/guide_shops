from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False, unique=True) # не повторяется
    psw = db.Column(db.String(500))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)
    avatar = db.Column(db.LargeBinary(), default=None)
    visit_shops_list = db.Column(db.LargeBinary(), default=None)
    added_shops_list = db.Column(db.LargeBinary(), default=None)
    edited_shops_list = db.Column(db.LargeBinary(), default=None)

    def __repr__(self):
        return f"<users {self.id}>"


from app import db

class ActionMixin:
    operator_id = db.Column(db.Integer, primary_key=True)
    time_stamp = db.Column(db.DateTime)

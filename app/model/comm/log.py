from app import db
from flask import request
from functools import wraps
from datetime import datetime
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote
from app.model.user import User
# 用户日志


class Log(db.Model):

    # 更改的log
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False) # 更改的表
    pre = db.Column(db.String(1024), nullable=False) # 修改前
    past = db.Column(db.String(1024), nullable=False) # 修改后

    note = db.Column(db.String(1024), default="")
    status = db.Column(db.Integer, default=2) # 0 不显示通过，1不显示未通过，2显示

    @property
    def user(self):
        t = User.query.filter(User.id == self.user_id).first()
        return t

    @staticmethod
    def log(user_id, target, past, note, pre="",):
        p = Log(user_id=user_id, target=target, pre=pre, past=past,note=note)
        db.session.add(p)
        db.session.commit()


    def to_json(self):
        return {
            'id':self.id,
            'timestamp':self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id':self.user_id,
            'target':self.target,
            'pre':self.pre,
            'past':self.past,
            'status': self.status,
            "note": self.note
        }

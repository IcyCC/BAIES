from app import db
from flask import request
from functools import wraps
from datetime import datetime
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote
from app.model.user import User
# 用户日志


class PutLog(db.Model):

    # 更改的log
    __tablename__ = "put_logs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False) # 更改的表
    pre = db.Column(db.String(1024), nullable=False) # 修改前
    past = db.Column(db.String(1024), nullable=False) # 修改后

    note = db.Column(db.String(1024), default="")
    status = db.Column(db.Integer, default=2) # 0 不显示通过，1不显示未通过，2显示

    user = db.relationship('User', primaryjoin=foreign(user_id) == remote(User.id),
                           lazy='joined', backref='put_logs')
    @staticmethod
    def log(user_id, target, pre, past, note):
        p = PutLog(user_id=user_id, target=target, pre=str(pre), past=str(past),note=note)
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
            'status': self.status
        }


class DeleteLog(db.Model):

    # 删除的log
    __tablename__ = "delete_logs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(1024),nullable=False) #　详细信息

    user = db.relationship('User', primaryjoin=foreign(user_id) == remote(User.id),
                           lazy='joined', backref='delete_logs')

    status = db.Column(db.Integer, default=2) # 0 不显示通过，1不显示未通过，2显示

    note = db.Column(db.String(1024), default="")
    @staticmethod
    def log(user_id, target, detail, note):
        p = DeleteLog(user_id=user_id, target=target, detail=str(detail), note=note)
        db.session.add(p)
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id': self.user_id,
            'target': self.target,
            'pre': self.pre,
            'past': self.past,
            'status': self.status
        }


class PostLog(db.Model):

    # 兴增的log
    __tablename__ = "post_logs"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(1024), nullable=False)

    status = db.Column(db.Integer, default=2) # 0 不显示通过，1不显示未通过，2显示
    user = db.relationship('User', primaryjoin=foreign(user_id) == remote(User.id),
                           lazy='joined', backref='post_logs')

    note = db.Column(db.String(1024), default="")

    @staticmethod
    def log(user_id, target, detail, note):
        p = PostLog(user_id=user_id, target=target, detail=detail, note=note)
        db.session.add(p)
        db.session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id': self.user_id,
            'target': self.target,
            'detail': self.detail,
            'status': self.status
        }



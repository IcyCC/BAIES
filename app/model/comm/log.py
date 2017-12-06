from app import db
from flask import request
from functools import wraps
from datetime import datetime

class PutLog(db.Model):

    __tablename__ = "put_log"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False)
    pre = db.Column(db.String(1024), nullable=False)
    past = db.Column(db.String(1024), nullable=False)

    @staticmethod
    def log(user_id, target, pre ,past):
        p = PutLog(user_id=user_id, target=target, pre=str(pre), past=str(past))
        db.Session.add(p)
        db.Session.commit()


    def to_json(self):
        return {
            'id':self.id,
            'timestamp':self.timestamp,
            'user_id':self.user_id,
            'target':self.target,
            'pre':self.pre,
            'past':self.past
        }


class DeleteLog(db.Model):
    __tablename__ = "delete_log"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(1024),nullable=False)

    @staticmethod
    def log(user_id, target, pre ,past):
        p = PutLog(user_id=user_id, target=target, pre=str(pre), past=str(past))
        db.Session.add(p)
        db.Session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'target': self.target,
            'pre': self.pre,
            'past': self.past
        }


class PostLog(db.Column):
    __tablename__ = "post_log"

    id = db.Column(db.Integer, primary_key=True, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(255), nullable=False)
    detail = db.Column(db.String(1024),nullable=False)

    @staticmethod
    def log(user_id, target, pre ,past):
        p = PutLog(user_id=user_id, target=target, pre=str(pre), past=str(past))
        db.Session.add(p)
        db.Session.commit()

    def to_json(self):
        return {
            'id': self.id,
            'timestamp': self.timestamp,
            'user_id': self.user_id,
            'target': self.target,
            'pre': self.pre,
            'past': self.past
        }



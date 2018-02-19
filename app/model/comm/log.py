from app import db
from flask import request
from functools import wraps
from datetime import datetime
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote
from app.model.user import User

# 用户日志


class SocLog(db.Model):

    # 更改的log
    __tablename__ = "soc_logs"

    id = db.Column(db.Integer, primary_key=True, index=True,autoincrement=True)
    note = db.Column(db.String(1024), default='')
    user_id = db.Column(db.Integer, index=True)
    table_id = db.Column(db.Integer, index=True)
    pre_log_id = db.Column(db.Integer,index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    @property
    def user(self):
        t = User.query.filter(User.id == self.user_id).first()
        return t

    @property
    def facts(self):
        from app.model.quantify.socioeconomic import SocioeconomicFacts
        t = SocioeconomicFacts.query.join(SocLog, SocLog.id == SocioeconomicFacts.log_id).\
            filter(SocLog.id == SocioeconomicFacts.log_id).all()
        return t

    @property
    def table(self):
        from app.model.quantify.socioeconomic import SocioeconomicTable
        t = SocioeconomicTable.query.filter(SocioeconomicTable.id == self.table_id).first()
        return t

    @property
    def pre_log(self):
        if self.pre_log == 0:
            return {
                "id": 0
            }
        log = SocLog.query.filter(SocLog.id == self.pre_log_id).first()
        return log

    def to_json(self):
        return {
            'id':self.id,
            'note': self.note,
            'user_id': self.user_id,
            'timestamp': self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'facts': [f.to_json() for f in self.facts],
            'table_id': self.table_id,
            'table': self.table.to_json_by_index()
        }


class ArgLog(db.Model):

    # 更改的log
    __tablename__ = "arg_logs"

    id = db.Column(db.Integer, primary_key=True, index=True,autoincrement=True)
    note = db.Column(db.String(1024), default='')
    user_id = db.Column(db.Integer, index=True)
    table_id = db.Column(db.Integer, index=True)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    # @property
    # def user(self):
    #     t = User.query.filter(User.id == self.user_id).first()
    #     return t
    #
    # @property
    # def facts(self):
    #     from app.model.quantify.agriculture_products import AgricultureFacts
    #     t = SocioeconomicFacts.join(SocLog, SocLog.id == SocioeconomicFacts.log_id).\
    #         filter(SocLog.id == SocioeconomicFacts.log_id).all()
    #     return t
    #
    # @property
    # def table(self):
    #     from app.model.quantify.socioeconomic import SocioeconomicTable
    #     t = SocioeconomicTable.query.filter(SocioeconomicTable.id == self.table_id).first()
    #     return t
    #
    # def to_json(self):
    #     return {
    #         'id':self.id,
    #         'note': self.note,
    #         'user_id': self.user_id,
    #         'timestamp': self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
    #         'facts': [f.to_json() for f in self.facts],
    #         'table_id': self.table_id,
    #         'table': self.table.to_json_by_index()
    #     }

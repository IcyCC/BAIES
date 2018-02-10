from app import db
from app.model.comm import ActionMixin
from datetime import datetime
from app.model.user import User
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote

# 定性信息

class Kind(db.Model):

    __tablename__ = "kinds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(64))
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cn_alis': self.cn_alis,
            'en_alis':self.en_alis,
            'posts': [p.to_json() for p in self.posts]
        }


class Post(db.Model):
    __tablename__ = "posts"
    # 文章信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)

    kind_id = db.Column(db.Integer)

    show = db.Column(db.Boolean, default=False)

    timestamp = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, nullable=False, index=True)

    kind = db.relationship('Kind', primaryjoin=foreign(kind_id) == remote(Kind.id),
                            backref='posts', lazy='joined')

    user = db.relationship('User', primaryjoin=foreign(user_id) == remote(User.id),
                           lazy='joined', backref='posts')

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'kind_id':self.kind_id,
            'timestamp':self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id':self.user_id,
            'show': self.show
        }
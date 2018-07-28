from app import db
from app.model.comm import ActionMixin
from datetime import datetime
from app.model.user import User,AnonymousUser
from app.model.quantify import Country
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote

# 定性信息

class Kind(db.Model):

    __tablename__ = "kinds"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, index=True)
    name = db.Column(db.String(64))
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    @staticmethod
    def r_query():
        return Kind.query

    @property
    def posts(self):
        t = Post.query.join(Kind, Kind.id == Post.kind_id).filter(Kind.id == Post.kind_id).all()
        return t


    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'cn_alis': self.cn_alis,
            'en_alis':self.en_alis,
            'posts': [p.to_json() for p in self.posts]
        }

    def to_json_simple(self):
        return {
            'id': self.id,
            'name': self.name,
            'cn_alis': self.cn_alis,
            'en_alis': self.en_alis,
        }

class Post(db.Model):
    __tablename__ = "posts"
    # 文章信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)

    country_id = db.Column(db.Integer, default=1, nullable=False)

    kind_id = db.Column(db.Integer, index=True)

    show = db.Column(db.Boolean, default=False)

    timestamp = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, nullable=False, index=True)

    img_url = db.Column(db.String(255), default='/')

    @staticmethod
    def r_query():
        return Post.query.join(User,
                               User.id == Post.user_id).join(
            Kind,
            Kind.id == Post.kind_id
        )

    @property
    def kind(self):
        t = Kind.query.filter(Kind.id == self.kind_id).first()
        return t

    @property
    def user(self):
        t = User.query.filter(User.id == self.user_id).first()
        return t

    @property
    def country(self):
        t = User.query.filter(Country.id == self.country_id).first()
        return t

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'kind_id':self.kind_id,
            'kind': self.kind.to_json_simple() if self.kind else {},
            'timestamp':self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id':self.user_id,
            'show': self.show,
            'user': self.user.to_json() if self.user is not None else AnonymousUser.to_json(),
            'img_url': self.img_url,
            'country_id': self.country_id,
        }

    def to_json_simple(self):
        return {
            'id': self.id,
            'title': self.title,
            'show': self.show,
            'kind_id': self.kind_id,
            'kind': self.kind.to_json_simple(),
            'timestamp': self.timestamp if self.timestamp is None else self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id': self.user_id,
            'img_url': self.img_url,
            'country_id': self.country_id,
        }


class Image(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    img_url = db.Column(db.String(128), default='/', nullable=False)
    to_url = db.Column(db.String(128),  default='/', nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False)

    @staticmethod
    def r_query():
        return Image.query

    def to_json(self):
        return {
            "id": self.id,
            "img_url": self.img_url,
            "to_url": self.to_url,
            "status": self.status
        }

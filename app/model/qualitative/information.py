from app import db
from app.model.comm import ActionMixin
from datetime import datetime
from app.model.user import User
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote

# 定性信息

class Post(db.Model):
    __tablename__ = "post"
    # 文章信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    en_title = db.Column(db.String(255)) # en　为英文
    en_body = db.Column(db.Text)
    kind = db.Column(db.String(64))
    en_kind = db.Column(db.String(64))

    timestamp = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, nullable=False, index=True)

    user = db.relationship('User', primaryjoin=foreign(user_id) == remote(User.id),
                           lazy='joined', backref='posts')

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'en_title': self.en_title,
            'en_body': self.en_body,
            'en_kind': self.en_kind,
            'kind':self.kind,
            'timestamp':self.time if self.time is None else self.time.strftime("%Y-%m-%d %H:%M:%S"),
            'user_id':self.user_id
        }
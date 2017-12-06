from app import db
from app.model.comm import ActionMixin
from datetime import datetime


class Post(db.Model):
    __tablename__ = "post"
    # 文章信息
    id = db.Column(db.Integer,primary_key=True,autoincrement=True,index=True)
    title = db.Column(db.String(255))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now())

    user_id = db.Column(db.Integer, nullable=False, index=True)

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'timestamp':self.timestamp,
            'user_id':self.user_id
        }
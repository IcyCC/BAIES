from app import db
from app.model.comm import ActionMixin
from datetime import datetime

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

    def to_json(self):
        return {
            'id':self.id,
            'title':self.title,
            'body':self.body,
            'en_title': self.en_title,
            'en_body': self.en_body,
            'en_kind': self.en_kind,
            'kind':self.kind,
            'timestamp':self.timestamp,
            'user_id':self.user_id
        }
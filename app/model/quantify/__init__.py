from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote


class Country(db.Model):
    __tablename__ = "countrys"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    en_alias = db.Column(db.String(255), index=True)
    cn_alias = db.Column(db.String(255), index=True)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "en_alias": self.en_alias,
            "cn_alias": self.cn_alias
        }



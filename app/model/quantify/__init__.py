from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote



class Country(db.Model):
    __tablename__ = "countrys"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    en_alis = db.Column(db.String(255), index=True)
    cn_alis = db.Column(db.String(255), index=True)

    @property
    def socioeconomic_facts(self):
        from .socioeconomic import SocioeconomicFacts
        t = Country.query.join(SocioeconomicFacts, Country.id == SocioeconomicFacts.country_id).filter(self.id == SocioeconomicFacts.country_id).all()
        return t

    @property
    def agriculture_facts(self):
        from .agriculture_products import AgricultureFacts
        t = Country.query.join(AgricultureFacts, Country.id == AgricultureFacts.country_id).filter(self.id == AgricultureFacts.country_id).all()
        return t

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "en_alis": self.en_alis,
            "cn_alis": self.cn_alis
        }



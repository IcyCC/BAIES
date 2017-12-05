from app import db


class AgricultureMixin:
    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country = db.Column(db.String(64), index=True)
    time = db.Column(db.DateTime)
    kind = db.Column(db.String(64))

    def get_agriculture_json(self):
        return {
            'id': self.id,
            'county': self.country,
            'time': self.time,
            'kind': self.kind
        }


class AgriculturalProductionProfiles(db.Model,AgricultureMixin):

    total = db.Column(db.Integer)

    def to_json(self):
        return {
           'total':self.total
        }.update(self.get_agriculture_json())



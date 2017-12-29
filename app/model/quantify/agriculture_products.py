from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote
from . import Country

class AgricultureTable(db.Model):
    __tablename__ = "agriculture_tables"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))



    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": str([i.to_json() for i in self.indexes])
        }

class AgricultureKind(db.Model):
    __tablename__ = "agriculture_kinds"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }




class AgricultureIndexes(db.Model):
    __tablename__ = "agriculture_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    unit = db.Column(db.String(255), default="no")

    table_id = db.Column(db.Integer, index=True)

    table = db.relationship('AgricultureTable', primaryjoin=foreign(table_id) == remote(table_id),
                              backref='table', lazy='joined')

    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table": self.table.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis
        }

    def fact_to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table_id": self.table_id,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis
        }

class AgricultureFacts(db.Model):

    __tablename__ = "agriculture_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, index=True)
    time = db.Column(db.DateTime, index=True)

    time_stamp = db.Column(db.DateTime, index=True)
    kind_id = db.Column(db.Integer, index=True)

    index_id = db.Column(db.Integer, index=True)
    value = db.Column(db.Float, index=True)

    index = db.relationship('AgricultureIndexes', primaryjoin=foreign(index_id) == remote(AgricultureIndexes.id),
                            backref='facts', lazy='joined')

    country = db.relationship('Country',
                               primaryjoin=foreign(country_id) == remote(Country.id),
                               backref='facts', lazy='joined')


    kind = db.relationship('AgricultureKind', primaryjoin=foreign(kind_id) == remote(AgricultureKind.id),
                           lazy='joined', backref='facts')

    def to_json(self):
        return {
            "id": self.id,
            "country": self.country.name,
            "time": self.time if self.time is None else self.time.strftime("%Y-%m-%d %H:%M:%S"),
            "time_stamp": self.time_stamp if self.time_stamp is None else self.time_stamp.strftime("%Y-%m-%d %H:%M:%S"),
            "kind": self.kind.name,
            "index": self.index.fact_to_json(),
            "value": self.value
        }

    @staticmethod
    def insert_data(tablename=None, country_name=None, time=None, index_name=None, value=None, kind=None):

        if tablename is None or country_name is None or index_name is None or kind is None:
            return None, "some filed is empty"
        index = AgricultureIndexes.query.filter_by(name=index_name).filter(AgricultureIndexes.table.name==tablename).first()
        country = Country.query.filter_by(name=country_name).first()
        kind = Country.query.filter_by(name=kind).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        if kind is None:
            return None, "table have`t this kind"

        s = AgricultureFacts(country_id=country.id, time=time,
                             index_id=index.id, value=value, kind_id=kind.id)

        db.session.add(s)
        db.session.commit()

        return s, ""

    @staticmethod
    def insert_data_with_id(table_id=None, country_id=None, time=None, index_id=None, kind_id=None,value=None):
        if table_id is None or country_id is None or index_id is None or kind_id is None:
            return None,"some filed is empty"
        index = AgricultureIndexes.query.filter_by(id=country_id).filter(AgricultureIndexes.table.id == table_id).first()
        country = Country.query.filter_by(id=index_id).first()
        kind = Country.query.filter_by(id=kind_id).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        if kind is None:
            return None, "table have`t this kind"

        s = AgricultureFacts(country_id=country.id, time=time,
                             index_id=index.id, value=value, kind_id=kind_id)

        db.session.add(s)
        db.session.commit()

        return s, ""

    @staticmethod
    def update(id=None,country_name=None, time=None, index_name=None, value=None, kind_name=None):

        if id is None or country_name is None or index_name is None:
            return None, "some filed is empty"

        fact = AgricultureFacts.query.filter_by(id=id).fisrt()

        if fact is None:
            return None, "no such fact"
        index = AgricultureFacts.query.filter_by(name=index_name).first()
        country = Country.query.filter_by(name=country_name).first()
        kind = AgricultureKind.query.filter_by(name=kind_name).first()

        fact.country_id = country.id
        fact.time = time
        fact.index_id = index.id
        fact.value = value
        fact.kind_id = kind.id
        db.session.add(fact)
        db.session.commit()
        return fact, ""

    @classmethod
    def find(cls, tablename=None, index=None, kind=None ,country=None, start_time=None, end_time=None):
        query = cls.query

        if tablename is not None:
            table = AgricultureIndexes.query.filter_by(name=tablename).first()
            if table is None:
                return []
            query = query.join(AgricultureIndexes, AgricultureKind.id == cls.kind_id).filter(AgricultureIndexes.table_id == table.id)

        if country is not None:
            query = query.join(Country, Country.id == cls.country_id).filter(Country.name == country)

        if index is not None:
            query = query.join(AgricultureIndexes, AgricultureIndexes.id == cls.index_id).filter(AgricultureIndexes.name == index)

        if kind is not None:
            query = query.join(AgricultureKind, AgricultureKind.id == cls.kind_id).filter(AgricultureKind.name == kind)

        if start_time is not None:
            query = query.filter(cls.time > start_time)

        if end_time is not None:
            query = query.filter(cls.time < end_time)

        return query.all()

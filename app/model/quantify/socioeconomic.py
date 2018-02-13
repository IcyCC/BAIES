from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_
from sqlalchemy.orm import foreign, remote
from . import Country

class SocioeconomicTable(db.Model):
    __tablename__ = "socioeconomic_tables"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    @property
    def indexes(self):
        t = SocioeconomicIndexes.query.join(SocioeconomicTable, SocioeconomicTable.id == SocioeconomicIndexes.table_id).filter(SocioeconomicIndexes.table_id == self.id).all()
        return t


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": [i.to_json_by_fact() for i in self.indexes]
        }

    def to_json_by_index(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": [i.id for i in self.indexes]
        }


class SocioeconomicIndexes(db.Model):
    __tablename__ = "socioeconomic_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    unit = db.Column(db.String(255), default="no")

    table_id = db.Column(db.Integer, index=True)

    # table = db.relationship('SocioeconomicTable', primaryjoin=foreign(table_id) == remote(SocioeconomicTable.id),
    #                         backref='indexes', lazy='joined'

    @property
    def table(self):
        t = SocioeconomicTable.query.filter(self.table_id == SocioeconomicTable.id).first()
        return t

    @property
    def facts(self):
        t = SocioeconomicIndexes.query.join(SocioeconomicFacts, SocioeconomicFacts.index_id == SocioeconomicIndexes.id).\
            filter(self.id == SocioeconomicFacts.index_id).all()
        return t

    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table_id": self.table_id,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
        }

    def to_json_by_fact(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table": self.table.to_json_by_index(),
            "table_id": self.table_id,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "facts": [i.id for i in self.facts]
        }




class SocioeconomicFacts(db.Model):

    __tablename__ = "socioeconomic_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer,index=True)
    time = db.Column(db.DateTime, index=True)

    time_stamp = db.Column(db.DateTime, index=True)

    index_id = db.Column(db.Integer, index=True)
    value = db.Column(db.Float)

    @property
    def index(self):
        t = SocioeconomicIndexes.query.filter(SocioeconomicIndexes.id == self.index_id).first()
        return t


    @property
    def country(self):
        t = Country.query.filter(Country.id == self.country_id).first()
        return t


    def to_json(self):

        return {
            "id": self.id,
            "country": self.country.to_json(),
            "time": self.time if self.time is None else self.time.strftime("%Y-%m-%d %H:%M:%S"),
            "value": self.value,
            "index_id": self.index_id,
            "time_stamp": self.time_stamp if self.time_stamp is None else self.time_stamp.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def insert_data(tablename=None, country_name=None, time=None, index_name=None, value=None):

        if tablename is None or country_name is None or index_name is None:
            return None, "some filed is empty"
        index = SocioeconomicIndexes.query.join(SocioeconomicTable, SocioeconomicTable.id == SocioeconomicIndexes.table_id).\
            filter(and_(
                        SocioeconomicIndexes.name == index_name,
                        SocioeconomicTable.name == tablename)).first()

        country = Country.query.filter_by(name=country_name).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        s = SocioeconomicFacts(country_id=country.id, time=time,
                               index_id=index.id, value=value)

        db.session.add(s)
        db.session.commit()

        return s,""

    @staticmethod
    def insert_data_with_id(table_id=None, country_id=None, time=None, index_id=None, value=None):
        if table_id is None or country_id is None or index_id is None:
            return None,"some filed is empty"
        table = SocioeconomicTable.query.filter_by(id=table_id).first()
        if table is None:
            return None, "no such id table"
        index = SocioeconomicIndexes.query.query.filter(SocioeconomicIndexes.table_id == table_id).first()
        country = Country.query.filter_by(id=index_id).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        s = SocioeconomicIndexes(country_id=country.id, time=time,
                                 index_id=index.id, value=value)

        db.session.add(s)
        db.session.commit()

        return s, ""

    @staticmethod
    def update(id=None,country_name=None, time=None, index_name=None, value=None ):

        if id is None or country_name is None or index_name is None:
            return None, "some filed is empty"

        fact = SocioeconomicFacts.query.filter_by(id=id).first()

        if fact is None:
            return None, "no such fact"
        index = SocioeconomicIndexes.query.filter_by(name=index_name).first()
        country = Country.query.filter_by(name=country_name).first()
        fact.country_id = country.id
        fact.time = time
        fact.index_id = index.id
        fact.value = value
        db.session.add(fact)
        db.session.commit()
        return fact, ""

    @staticmethod
    def update_with_id(id=None, country_id=None, time=None, index_id=None, value=None):

        if id is None or country_id is None or index_id is None  or value is None:
            return None, "some filed is empty"

        fact = SocioeconomicFacts.query.filter_by(id=id).fisrt()

        if fact is None:
            return None, "no such fact"
        index = SocioeconomicFacts.query.filter_by(id=index_id).first()
        country = Country.query.filter_by(id=country_id).first()

        fact.country_id = country.id
        fact.time = time
        fact.index_id = index.id
        fact.value = value
        db.session.add(fact)
        db.session.commit()
        return fact, ""


    @classmethod
    def find(cls, table_id=None, index_ids=None,country_ids=None, start_time=None, end_time=None):
        query = cls.query

        if table_id is not None:
            table = SocioeconomicTable.query.filter_by(id=table_id).first()
            if table is None:
                return []
            query = query.join(SocioeconomicIndexes, SocioeconomicIndexes.id == cls.index_id).filter(SocioeconomicIndexes.table_id == table.id)

        if country_ids is False or country_ids is not None:
            query = query.join(Country, Country.id == cls.country_id).filter(Country.id.in_(country_ids))

        if index_ids is False or index_ids is not None:
            query = query.filter(SocioeconomicIndexes.id.in_(index_ids))

        if start_time is not None:
            query = query.filter(cls.time >= start_time)

        if end_time is not None:
            query = query.filter(cls.time <= end_time)

        return query.all()

    @classmethod
    def find_one(cls, table_id=None, index_id=None,country_id=None, time=None):
        query = cls.query

        if table_id is not None:
            table = SocioeconomicTable.query.filter_by(id=table_id).first()
            if table is None:
                return []
            query = query.join(SocioeconomicIndexes, SocioeconomicIndexes.id == cls.index_id).filter(SocioeconomicIndexes.table_id == table.id)

        if country_id is not None:
            query = query.join(Country, Country.id == cls.country_id).filter(Country.id == country_id)

        if index_id is not None:
            query = query.filter(SocioeconomicIndexes.id == index_id)

        if time is not None:
            query = query.filter(cls.time == time)

        return query.first()




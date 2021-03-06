from app import db
from app.model.comm.log import ArgLog
from flask import jsonify
from sqlalchemy.sql.expression import and_,or_
from sqlalchemy.orm import foreign, remote
from . import Country
from datetime import datetime


class AgricultureTable(db.Model):
    __tablename__ = "agriculture_tables"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))
    cur_log_id = db.Column(db.Integer, index=True, default=0)

    @staticmethod
    def r_query():
        return AgricultureTable.query

    @property
    def indexes(self):
        t = AgricultureIndexes.query.join(AgricultureTable, AgricultureTable.id == AgricultureIndexes.table_id).filter(AgricultureIndexes.table_id == self.id).all()
        return t


    @property
    def cur_log(self):
        log = ArgLog.query.filter(ArgLog.id == self.cur_log_id).first()
        return log


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": [i.to_json() for i in self.indexes]
        }

    def to_json_by_index(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": [i.id for i in self.indexes]
        }

class AgricultureKind(db.Model):
    __tablename__ = "agriculture_kinds"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    en_alis = db.Column(db.String(255))
    cn_alis = db.Column(db.String(255))

    @staticmethod
    def r_query():
        return AgricultureTable.query

    @property
    def facts(self):
        t = AgricultureFacts.query.join(AgricultureKind, AgricultureKind.id == AgricultureFacts.kind_id).filter(self.id == AgricultureFacts.kind_id).all()
        return t

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "facts": [i.to_json() for i in self.facts]
        }

    def to_json_by_fact(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis
        }




class AgricultureIndexes(db.Model):
    __tablename__ = "agriculture_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    unit = db.Column(db.String(255), default="no")

    table_id = db.Column(db.Integer, index=True)

    @staticmethod
    def r_query():
        return AgricultureIndexes.join(AgricultureTable, AgricultureTable.id ==AgricultureIndexes.table_id)

    @property
    def table(self):
        t = AgricultureTable.r_query().filter(self.table_id == AgricultureTable.id).first()
        return t

    @property
    def facts(self):
        t = AgricultureFacts.query.join(AgricultureIndexes, AgricultureIndexes.id == AgricultureFacts.index_id).filter(self.id == AgricultureFacts.index_id).all()
        return t

    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table": self.table.to_json_by_index(),
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "facts": [i.to_json() for i in self.facts]
        }

    def to_json_by_fact(self):
        return {
            "id": self.id,
            "name": self.name,
            "unit": self.unit,
            "table": self.table.to_json_by_index(),
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis
        }

class AgricultureFacts(db.Model):

    __tablename__ = "agriculture_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, index=True)
    time = db.Column(db.Integer, index=True)

    time_stamp = db.Column(db.DateTime, index=True, default=datetime.now())
    kind_id = db.Column(db.Integer, index=True)

    index_id = db.Column(db.Integer, index=True)
    value = db.Column(db.Float, index=True)

    log_id = db.Column(db.Integer, index=True, autoincrement=True)


    @staticmethod
    def r_query():
        return AgricultureFacts.query.join(Country, Country.id == AgricultureFacts.country_id).join(AgricultureKind, AgricultureKind.id==AgricultureFacts.kind_id).join(AgricultureIndexes, AgricultureIndexes.id == AgricultureFacts.index_id)

    @property
    def index(self):
        t = AgricultureIndexes.query.join(AgricultureFacts, AgricultureFacts.index_id ==AgricultureIndexes.id).filter(AgricultureIndexes.id == self.index_id).first()
        return t

    @property
    def country(self):
        t = Country.r_query().filter(Country.id == self.country_id).first()
        return t

    @property
    def log(self):
        t = ArgLog.r_query().filter(ArgLog.id == self.log_id).first()
        return t

    @property
    def kind(self):
        t = AgricultureKind.r_query().filter(AgricultureKind.id == self.kind_id).first()
        return t

    def to_json(self):
        return {
            "id": self.id,
            "country_id": self.country_id,
            "time": self.time ,
            "value": self.value,
            "index_id": self.index_id,
            "kind_id": self.kind_id,
            "log_id": self.log_id,
            "time_stamp": self.time_stamp if self.time_stamp is None else self.time_stamp.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def insert_data(tablename=None, country_name=None, time=None, index_name=None, value=None, kind=None):

        if tablename is None or country_name is None or index_name is None or kind is None:
            return None, "some filed is empty"
        index = AgricultureIndexes.r_query().filter(AgricultureIndexes.name==index_name).filter(AgricultureIndexes.table.name==tablename).first()
        country = Country.r_query().filter(Country.name==country_name).first()
        kind = Country.r_query().filter(AgricultureKind.name==kind).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        if kind is None:
            return None, "table have`t this kind"

        s = AgricultureFacts(country_id=country.id, time=time,
                             index_id=index.id, value=value, kind_id=kind.id)

        Country.r_query().filter(Country.id.in_())

        db.session.add(s)
        db.session.commit()

        return s, ""

    @staticmethod
    def insert_data_with_id(table_id=None, country_id=None, time=None, index_id=None, kind_id=None,value=None):
        if table_id is None or country_id is None or index_id is None or kind_id is None:
            return None,"some filed is empty"
        table = AgricultureTable.r_query().filter(AgricultureTable.id==table_id).first()
        if table is None:
            return None, "no such id table"
        index = AgricultureIndexes.r_query().filter(AgricultureIndexes.table_id == table_id).first()
        country = Country.r_query().filter(Country.id==index_id).first()
        kind = Country.r_query().filter(Country.id==kind_id).first()

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

        fact = AgricultureFacts.r_query().filter(AgricultureFacts.id==id).fisrt()

        if fact is None:
            return None, "no such fact"
        index = AgricultureFacts.r_query().filter(AgricultureFacts.name==index_name).first()
        country = Country.r_query().filter(Country.name==country_name).first()
        kind = AgricultureKind.r_query().filter(AgricultureKind.name==kind_name).first()

        fact.country_id = country.id
        fact.time = time
        fact.index_id = index.id
        fact.value = value
        fact.kind_id = kind.id
        db.session.add(fact)
        db.session.commit()
        return fact, ""

    @staticmethod
    def update_with_id(id=None, country_id=None, time=None, index_id=None, value=None, kind_id=None):

        if id is None or country_id is None or index_id is None or kind_id is None or value is None:
            return None, "some filed is empty"

        fact = AgricultureFacts.r_query().filter(AgricultureFacts.id==id).fisrt()

        if fact is None:
            return None, "no such fact"
        index = AgricultureFacts.r_query().filter(AgricultureFacts.id==index_id).first()
        country = Country.r_query().filter(Country.id==country_id).first()
        kind = AgricultureKind.r_query().filter(AgricultureKind.id==kind_id).first()

        fact.country_id = country.id
        fact.time = time
        fact.index_id = index.id
        fact.value = value
        fact.kind_id = kind.id
        db.session.add(fact)
        db.session.commit()
        return fact, ""

    @classmethod
    def find(cls, table_id=None, kind_ids=None, index_ids=None,country_ids=None, start_time=None, end_time=None, log_id = None):
        query = cls.r_query()

        if table_id is not None:
            table = AgricultureTable.r_query().filter(AgricultureTable.id==table_id).first()
            if table is None:
                return []
            query = query.join(AgricultureIndexes, AgricultureIndexes.id == cls.index_id).filter(AgricultureIndexes.table_id == table.id)

        if country_ids is False or country_ids is not None:
            query = query.filter(AgricultureFacts.country_id.in_(country_ids))

        if index_ids is False or index_ids is not None:
            query = query.filter(AgricultureFacts.index_id.in_(index_ids))

        if kind_ids is False or kind_ids is not None:
            query = query.filter(AgricultureFacts.kind_id.in_(kind_ids))

        if start_time is not None:
            query = query.filter(cls.time >= start_time)

        if end_time is not None:
            query = query.filter(cls.time <= end_time)

        if log_id is not None:
            query = query.filter(cls.log_id == log_id)

        return query.all()

    @classmethod
    def find_one(cls, table_id=None, index_id=None,country_id=None, time=None, kind_id= None, log_id=None):
        query = cls.r_query()

        if table_id is not None:
            table = AgricultureTable.r_query().filter(AgricultureTable.id==table_id).first()
            if table is None:
                return []
            query = query.join(AgricultureIndexes, AgricultureIndexes.id == cls.index_id).filter(AgricultureIndexes.table_id == table.id)

        if country_id is not None:
            query = query.join(Country, Country.id == cls.country_id).filter(Country.id == country_id)

        if index_id is not None:
            query = query.filter(AgricultureIndexes.id == index_id)

        if time is not None:
            query = query.filter(AgricultureFacts.time == time)

        if kind_id is not None:
            query = query.filter(AgricultureFacts.kind_id == kind_id)

        if log_id is not None:
            query = query.filter(AgricultureFacts.log_id == log_id)

        return query.first()
from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_


class SocioeconomicFacts(db.Model):

    __tablename__ = "socioeconomic_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey("countrys.id"))
    time = db.Column(db.DateTime, index=True)

    time_stamp = db.Column(db.DateTime, index=True)

    index_id = db.Column(db.Integer, db.ForeignKey('socioeconomic_indexes.id'))
    value = db.Column(db.Float)

    def to_json(self):

        return {
            "id": self.id,
            "country": self.country.name,
            "time": self.time,
            "value": self.value,
            "index": self.index.fact_to_json(),
            "time_stamp": self.time_stamp
        }

    @staticmethod
    def insert_data(tablename=None, country_name=None, time=None, index_name=None, value=None):

        if tablename is None or country_name is None or index_name is None:
            return None, "some filed is empty"
        index = SocioeconomicIndexes.query.join(SocioeconomicTable).\
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
        index = SocioeconomicIndexes.query.filter_by(id=country_id).filter(SocioeconomicIndexes.table.id == table_id).first()
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

        fact = SocioeconomicFacts.query.filter_by(id=id).fisrt()

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


    @classmethod
    def find(cls, tablename=None, index=None,country=None, start_time=None, end_time=None):
        query = cls.query

        if tablename is not None:
            table = SocioeconomicTable.query.filter_by(name=tablename).first()
            if table is None:
                return []
            query = query.join(SocioeconomicIndexes).filter(SocioeconomicIndexes.table_id == table.id)

        if country is not None:
            query = query.join(Country).filter(Country.name == country)

        if index is not None:
            query = query.join(SocioeconomicIndexes).filter(SocioeconomicIndexes.name == index)

        if start_time is not None:
            query = query.filter(cls.time > start_time)

        if end_time is not None:
            query = query.filter(cls.time < end_time)

        return query.all()





class AgricultureFacts(db.Model):

    __tablename__ = "agriculture_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey("countrys.id"))
    time = db.Column(db.DateTime, index=True)

    time_stamp = db.Column(db.DateTime, index=True)
    kind_id = db.Column(db.Integer, db.ForeignKey("agriculture_kinds.id"))

    index_id = db.Column(db.Integer,  db.ForeignKey('agriculture_indexes.id'))
    value = db.Column(db.Float, index=True)

    def to_json(self):
        return {
            "id": self.id,
            "country": self.country.name,
            "time": self.time,
            "time_stamp": self.time_stamp,
            "kind": self.kind.name,
            "index": self.index.fact_to_json(),
            "value": self.value
        }

    @staticmethod
    def insert_data(tablename=None, country_name=None, time=None, index_name=None, value=None):

        if tablename is None or country_name is None or index_name is None:
            return None, "some filed is empty"
        index = AgricultureIndexes.query.filter_by(name=index_name).filter(AgricultureIndexes.table.name==tablename).first()
        country = Country.query.filter_by(name=country_name).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        s = AgricultureFacts(country_id=country.id, time=time,
                             index_id=index.id, value=value)

        db.session.add(s)
        db.session.commit()

        return s, ""

    @staticmethod
    def insert_data_with_id(table_id=None, country_id=None, time=None, index_id=None, value=None):
        if table_id is None or country_id is None or index_id is None:
            return None,"some filed is empty"
        index = AgricultureIndexes.query.filter_by(id=country_id).filter(SocioeconomicIndexes.table.id == table_id).first()
        country = Country.query.filter_by(id=index_id).first()

        if index is None:
            return None, "table have`t this index"

        if country is None:
            return None, "table have`t this country"

        s = AgricultureFacts(country_id=country.id, time=time,
                             index_id=index.id, value=value)

        db.session.add(s)
        db.session.commit()

        return s, ""

    @classmethod
    def find(cls, tablename=None, index=None, kind=None ,country=None, start_time=None, end_time=None):
        query = cls.query

        if tablename is not None:
            table = AgricultureIndexes.query.filter_by(name=tablename).first()
            if table is None:
                return []
            query = query.join(AgricultureIndexes).filter(AgricultureIndexes.table_id == table.id)

        if country is not None:
            query = query.join(Country).filter(Country.name == country)

        if index is not None:
            query = query.join(AgricultureIndexes).filter(AgricultureIndexes.name == index)

        if kind is not None:
            query = query.join(AgricultureKind).filter(AgricultureKind.name == kind)

        if start_time is not None:
            query = query.filter(cls.time > start_time)

        if end_time is not None:
            query = query.filter(cls.time < end_time)

        return query.all()

class SocioeconomicIndexes(db.Model):

    __tablename__ = "socioeconomic_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    unit = db.Column(db.String(255), default="no")

    table_id = db.Column(db.Integer, db.ForeignKey("socioeconomic_tables.id"))

    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    facts = db.relationship('SocioeconomicFacts', primaryjoin=(SocioeconomicFacts.index_id ==id) ,backref='index', lazy='joined')

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

class AgricultureIndexes(db.Model):

    __tablename__ = "agriculture_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    unit = db.Column(db.String(255), default="no")

    table_id = db.Column(db.Integer, db.ForeignKey("agriculture_tables.id"))

    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    facts = db.relationship('AgricultureFacts',primaryjoin=(AgricultureFacts.index_id ==id), backref='index', lazy='joined')

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



class SocioeconomicTable(db.Model):
    __tablename__ = "socioeconomic_tables"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    indexes = db.relationship('SocioeconomicIndexes' ,backref='table', lazy='joined')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": str([i.to_json() for i in self.indexes])
        }

class AgricultureTable(db.Model):
    __tablename__ = "agriculture_tables"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    cn_alis = db.Column(db.String(255))
    en_alis = db.Column(db.String(255))

    indexes = db.relationship('AgricultureIndexes', backref='table', lazy='joined')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "cn_alis": self.cn_alis,
            "en_alis": self.en_alis,
            "indexes": str([i.to_json() for i in self.indexes])
        }


class Country(db.Model):

    __tablename__= "countrys"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)

    agriculture_facts = db.relationship('AgricultureFacts', backref='countries', lazy='joined')

    socioeconomic_facts = db.relationship('SocioeconomicFacts',
                                          backref='country', lazy='joined')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }


class AgricultureKind(db.Model):

    __tablename__ = "agriculture_kinds"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)

    facts = db.relationship('AgricultureFacts', lazy='joined',backref='kind')

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
        }
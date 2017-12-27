from app import db
from app.model.comm import ActionMixin
from flask import jsonify
from sqlalchemy.sql.expression import and_


class SocioeconomicFacts(db.Model):

    __tablename__ = "socioeconomic_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, index=True, nullable=False)
    time = db.Column(db.DateTime, index=True)

    index_id = db.Column(db.Integer, db.ForeignKey('socioeconomic_indexes.id'))
    value = db.Column(db.Float)

    item_id = db.Column(db.Integer, index=True)

    @staticmethod
    def insert_data(table, index, **kwargs):
        index = SocioeconomicIndexes.query.filter_by(name=index).filter_by(table=table).first()

        if index is None:
            return jsonify(status="fail", reason="table have`t this index", data=[])

        s = AgricultureFacts(country=kwargs.get("country"), time=kwargs.get("time"),
                               index_id=index.id, value=kwargs.get("value"),item_id=kwargs.get("item_id"))

        db.session.add(s)
        db.session.commit()

        return s

    @staticmethod
    def get_all_table(detail=False):
        resp = db.session.execute("SELECT sheet FROM socioeconomic_indexes GROUP  BY sheet").fetchall()
        tables = map(lambda item: item[0], resp)
        if not detail:
            return tables
        else:
            result = list()
            for table in tables:
                indexes = AgricultureIndexes.query.filter_by(sheet=table).all()
                result.append({'table': table, 'indexes': [{'name': index.name, 'id': index.id} for index in indexes]})
            return result

    @staticmethod
    def find(tablename, **kwargs):
        query = AgricultureFacts.query.filter(AgricultureIndexes.sheet == tablename)
        allow_ids = set()

        for k, v in kwargs.items():
            resp = db.session.execute("SELECT item_id FROM agriculture_facts WHERE value = :value AND index_id IN "
                                      "(SELECT id FROM agriculture_indexes WHERE name= :name AND sheet = :sheet)",
                                            {'value':v,'name':k,'sheet':tablename}).fetchall()
            for i in resp:
                if i[0] is not None:
                    allow_ids.add(i[0])

        query = query.filter(AgricultureFacts.item_id.in_(allow_ids))
        items = query.all()
        ids = set()
        result = dict()
        for item in items:
            if item.item_id in ids:
                result[item.item_id].update({item.index.name:item.value})
            else:
                result.update({item.item_id: {item.index.name:item.value}})
                ids.add(item.item_id)
        return result

    @staticmethod
    def get_item_num():
        resp = db.session.execute("select max(item_id) From agriculture_facts").fetchall()
        if resp[0][0] is None:
            return 1
        return resp[0][0]




class AgricultureFacts(db.Model):

    __tablename__ = "agriculture_facts"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    country_id = db.Column(db.Integer, index=True, nullable=False)
    time = db.Column(db.DateTime)
    kind_id = db.Column(db.Integer, index=True)

    index_id = db.Column(db.Integer,  db.ForeignKey('agriculture_indexes.id'))
    value = db.Column(db.Integer, index=True)

    item_id = db.Column(db.Integer, index=True)

    @staticmethod
    def insert_data(table, index, **kwargs):
        index = AgricultureIndexes.query.filter_by(name=index).filter_by(table=table).first()

        if index is None:
            return jsonify(status="fail", reason="table have`t this index", data=[])

        s = AgricultureFacts(country=kwargs.get("country"), time=kwargs.get("time"),
                               index_id=index.id, value=kwargs.get("value"),item_id=kwargs.get("item_id"))

        db.session.add(s)
        db.session.commit()

        return s

    @staticmethod
    def get_all_table(detail=False):
        resp = db.session.execute("SELECT sheet FROM agriculture_indexes GROUP  BY sheet").fetchall()
        tables = map(lambda item: item[0], resp)
        if not detail:
            return tables
        else:
            result = list()
            for table in tables:
                indexes = AgricultureIndexes.query.filter_by(sheet=table).all()
                result.append({'table': table, 'indexes': [{'name': index.name, 'id': index.id} for index in indexes]})
            return result

    @staticmethod
    def find(tablename, **kwargs):
        query = AgricultureFacts.query.join(AgricultureIndexes,AgricultureFacts.index_id == AgricultureIndexes.id)\
            .filter(AgricultureIndexes.sheet == tablename)
        allow_ids = set()

        for k, v in kwargs.items():
            resp = db.session.execute("SELECT item_id FROM agriculture_facts WHERE value = :value AND index_id IN "
                                      "(SELECT id FROM agriculture_indexes WHERE name= :name AND sheet = :sheet)",
                                            {'value':v,'name':k,'sheet':tablename}).fetchall()
            for i in resp:
                if i[0] is not None:
                    allow_ids.add(i[0])

        query = query.filter(AgricultureFacts.item_id.in_(allow_ids))
        items = query.all()
        ids = set()
        result = dict()
        for item in items:
            if item.item_id in ids:
                result[item.item_id].update({item.index.name:item.value})
            else:
                result.update({item.item_id: {item.index.name:item.value}})
                ids.add(item.item_id)
        return result

    @staticmethod
    def get_item_num():
        resp = db.session.execute("select max(item_id) From agriculture_facts").fetchall()
        if resp[0][0] is None:
            return 1
        return resp[0][0]


class SocioeconomicIndexes(db.Model):

    __tablename__ = "socioeconomic_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    sheet = db.Column(db.String(255), index=True, nullable=False)

    facts = db.relationship('SocioeconomicFacts', primaryjoin=(SocioeconomicFacts.index_id ==id) ,backref='index', lazy='joined')


class AgricultureIndexes(db.Model):

    __tablename__ = "agriculture_indexes"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)
    sheet = db.Column(db.String(255), index=True, nullable=False)

    facts = db.relationship('AgricultureFacts',primaryjoin=(AgricultureFacts.index_id ==id), backref='index', lazy='joined')


class Country(db.Model):

    __tablename__= "countrys"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)

    agriculture_facts = db.relationship('AgricultureFacts', primaryjoin=(AgricultureFacts.country_id == id),
                                        backref='country', lazy='joined')

    socioeconomic_facts = db.relationship('SocioeconomicFacts', primaryjoin=(AgricultureFacts.country_id == id),
                                          backref='country', lazy='joined')


class AgricultureKind(db.Model):

    __tablename__ = "agriculture_kinds"

    id = db.Column(db.Integer, primary_key=True, index=True, autoincrement=True)
    name = db.Column(db.String(255), index=True, nullable=False)

    facts = db.relationship('AgricultureFacts', primaryjoin=(AgricultureFacts.country_id == id),
                            backref='kind', lazy='joined')
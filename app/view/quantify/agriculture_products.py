from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify import Country
from app.model.quantify.agriculture_products import AgricultureIndexes,AgricultureKind,AgricultureFacts,AgricultureTable
from app.model.user import Permission
from flask_login import current_user
from app.model.comm.log import PutLog,DeleteLog,PostLog
import json
import sqlalchemy

ALLOW_ARGS = (
    "tablename",
    "country",
    "index",
    "start_time",
    "end_time",
    "batch",
    "kind"
)

def check_args(father,son):

    return set(father) > set(son)


@quantify_blueprint.route("/agriculture_facts", methods=['GET', 'POST','PUT', 'DELETE'])
def agriculture_facts():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = request.args

        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])
        facts =  AgricultureFacts.find(tablename=args.get("tablename"), index=args.get("index"),
                                          country=args.get("country"), start_time=args.get("start_time"))

        result = dict()

        for fact in facts:
            if result.get(fact.index_id) is None:
                result.update({fact.index_id: [fact.to_json()]})
            else:
                result[fact.index_id].append(fact.to_json())

        return jsonify(status="success", reason="", data=result)

    if request.method == "POST":

        if request.args.get("batch") is None:

            fact, detail = AgricultureFacts.insert_data(tablename=request.form.get("tablename"),
                                                        country_name=request.form.get("country"),
                                                        time=request.form.get("time"),
                                                        index_name=request.form.get("index"),
                                                        value=request.form.get("value"),
                                                        kind=request.form.get("kind"))

            if fact is None:
                return jsonify(status="fail", reason=detail, data=[])
            PostLog.log(user_id=current_user.id, target=request.form.get("tablename"), detail=str(fact.to_json()),
                        note=request.form.get("note",""))
            return jsonify(status="success", reason="", data=[fact.to_json()])

        else:
            body = request.json
            data = body.get("data")

            for item in data:

                # body:
                # {tablename:"", data:[], note: ""}

                fact, detail = AgricultureFacts.insert_data(tablename=body.get("tablename"),
                                                            country_name=item.get("country"),
                                                            time=item.get("time"),
                                                            index_name=item.get("index"),
                                                            value=item.get("value"),
                                                            kind=item.get("kind"))
                if fact is None:
                    return jsonify(status="fail", reason="some"+detail, data=[])
                PostLog.log(current_user.id, detail=str(fact.to_json()), note=body.get("note",""), target=body.get("tablename"))
            return jsonify(status="success", reason="", data=[])

    if request.method == "PUT":
        body = request.json

        for item in body.get("data"):

            # body:
            # {tablename:"", data:[], note: ""}
            pre_fact = AgricultureFacts.query.filter_by(id=item.get("id")).first()

            fact, detail = AgricultureFacts.update(id=item.get("id"),
                                                   country_name=item.get("country"),
                                                   time=item.get("time"),
                                                   index_name=item.get("index"),
                                                   value=item.get("value"),
                                                   kind_name=item.get("kind"))

            if fact is None:
                return jsonify(status="fail", reason="some" + detail, data=[])
            PutLog.log(current_user.id, pre=str(pre_fact.to_json()), past=str(fact.to_json()), note=body.get("note",""),
                       target=body.get("tablename"))
        return jsonify(status="success", reason="", data=[])

    if request.method == "DELETE":

        list_str = request.form.get("list")
        note = request.form.get("note","")

        if list_str is None:
            return jsonify(status="fail", reason="list or tablename cant`t be empty", data=[])

        fact_ids = json.loads(list_str)
        deleted_facts = list()

        for id in fact_ids:
            fact = AgricultureFacts.query.filter_by(id=id).first()
            if fact is None:
                return jsonify(status="fail", reason="no id :{} fact".format(str(id)), data=[])
            deleted_facts.append(fact)

        for fact in deleted_facts:
            db.session.delete(fact)
            db.session.commit()

            DeleteLog.log(current_user.id, target=fact.index.table.name, detail=str(fact.to_json()),note=note)

        return jsonify(status="success", reason="", data=[f.to_json() for f in deleted_facts])


@quantify_blueprint.route("/agriculture_table", methods=['GET', 'POST','PUT', 'DELETE'])
def agriculture_table():
    if request.method == "GET":
        tables = AgricultureTable.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in tables])

    if request.method == "POST":
        table = AgricultureTable(name=request.form.get("name"),
                                   cn_alis=request.form.get("cn_alis"),
                                   en_alis=request.form.get("en_alis"))

        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "DELETE":

        table = AgricultureTable.query.filter_by(id=request.args.get("id")).first()
        db.session.delete(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])


@quantify_blueprint.route("/agriculture_index", methods=['GET', 'POST','PUT', 'DELETE'])
def agriculture_index():
    if request.method == "GET":
        indexes = AgricultureTable.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in indexes])

    if request.method == "POST":
        index = AgricultureIndexes(name=request.form.get("name"),
                                   cn_alis=request.form.get("cn_alis"),
                                   en_alis=request.form.get("en_alis"),
                                   unit=request.form.get("unit"),
                                   table_id=request.form.get("table_id"))

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "PUT":
        index = AgricultureIndexes.query.filter_by(id=request.form.get("id")).first()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "DELETE":

        index = AgricultureIndexes.query.filter_by(id=request.args.get("id")).first()
        db.session.delete(index)
        db.session.commit()
        return jsonify(status="success", reason="", data=[index.to_json()])
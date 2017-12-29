from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify import SocioeconomicFacts,Country,SocioeconomicIndexes,SocioeconomicTable
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
    "batch"
)

def check_args(father,son):

    return set(father) > set(son)

@quantify_blueprint.route("/socioeconomic_facts", methods=['GET', 'POST'])
def socioeconomic_facts():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = request.args

        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        result = [fact.to_json() for fact in SocioeconomicFacts.find(tablename=args.get("tablename"), index=args.get("index"),
                                          country=args.get("country"), start_time=args.get("start_time"),
                                          end_time=args.get("end_time"))]
        return jsonify(status="success", reason="", data=result)

    if request.method == "POST":

        if request.args.get("batch") is None:

            fact, detail = SocioeconomicFacts.insert_data(tablename=request.form.get("tablename"),
                                                          country_name=request.form.get("country_name"),
                                                          time=request.form.get("time"),
                                                          index_name=request.form.get("index_name"),
                                                          value=request.form.get("value"))

            if fact is None:
                return jsonify(status="fail", reason=detail, data=[])
            PostLog.log(user_id=current_user.id, target=request.form.get("tablename"), detail=str(fact.to_json()),
                        note=request.form.get("note"))
            return jsonify(status="success", reason="", data=[fact.to_json()])

        else:
            body = request.json
            data = body.get("data")
            for item in data:

                # body:
                # {tablename:"", data:[], note: ""}

                fact, detail = SocioeconomicFacts.insert_data(tablename=body.get("tablename"),
                                                              country_name=item.get("country"),
                                                              time=item.get("time"),
                                                              index_name=item.get("index"),
                                                              value=item.get("value"))
                if fact is None:
                    return jsonify(status="fail", reason="some"+detail, data=[])
            PostLog.log(current_user.id, detail=str(body.get("data")), note=body.get("note"), target=body.get("tablename"))
            return jsonify(status="success", reason="", data=[])

    if request.method == "PUT":
        body = request.json()

        for item in body.data:

            # body:
            # {tablename:"", data:[], note: ""}

            fact, detail = SocioeconomicFacts.update(id=item.id,
                                                     country_name=item.country,
                                                     time=item.time,
                                                     index_name=item.index,
                                                     value=item.value)

            if fact is None:
                return jsonify(status="fail", reason="some" + detail, data=[])
            PostLog.log(current_user.id, detail=str(fact.to_json()), note=body.get("note"), target=body.get("tablename"))
        return jsonify(status="success", reason="", data=[])

    if request.method == "DELETE":
        list_str = request.args.get("list")
        if list_str is None:
            return jsonify(status="fail", reason="list cant`t be empty", data=[])
        fact_ids = json.loads(list_str)
        deleted_facts = list()
        for id in fact_ids:
            fact = SocioeconomicFacts.filter()


@quantify_blueprint.route("/socioeconomic_table", methods=['GET', 'POST'])
def socioeconomic_table():
    if request.method == "GET":
        tables = SocioeconomicTable.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in tables])

    if request.method == "POST":
        table = SocioeconomicTable(name=request.form.get("name"),
                                   cn_alis=request.form.get("cn_alis"),
                                   en_alis=request.form.get("en_alis"))

        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "DELETE":

        table = SocioeconomicTable.filter_by(id=request.args.get("id")).first()
        db.session.delete(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])


@quantify_blueprint.route("/socioeconomic_index", methods=['GET', 'POST'])
def socioeconomic_index():
    if request.method == "GET":
        indexes = SocioeconomicIndexes.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in indexes])

    if request.method == "POST":
        index = SocioeconomicIndexes(name=request.form.get("name"),
                                     cn_alis=request.form.get("cn_alis"),
                                     en_alis=request.form.get("en_alis"),
                                     unit=request.form.get("unit"))

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "PUT":
        index = SocioeconomicIndexes.filter_by(id=request.form.get("id")).first()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "DELETE":

        index = SocioeconomicIndexes.filter_by(id=request.args.get("id")).first()
        db.session.delete(index)
        db.session.commit()
        return jsonify(status="success", reason="", data=[index.to_json()])
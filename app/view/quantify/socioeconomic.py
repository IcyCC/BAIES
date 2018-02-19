from flask import request, jsonify, current_app
from app import db, std_json
from . import quantify_blueprint
from app.model.quantify import Country
from app.model.quantify.socioeconomic import SocioeconomicFacts,SocioeconomicIndexes,SocioeconomicTable
from app.model.user import Permission
from flask_login import current_user
from app.model.comm.log import SocLog
import json
from datetime import datetime
import sqlalchemy

ALLOW_ARGS = (
    "tablename",
    "table_id",
    "country",
    "index",
    "start_time",
    "end_time",
    "batch",
    "country_ids",
    "index_ids",
    "log_id"
)

def check_args(father,son):

    return set(father) > set(son)

def find_in_list(items, id, func):
    for item in items:
        if func(item, id):
            return item

    return None

@quantify_blueprint.route("/socioeconomic_facts", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_facts():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = std_json(request.args)


        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        start_time = args.get("start_time")
        # if start_time is not None:
        #     start_time = datetime.strptime(str(start_time), "%Y")

        end_time = args.get("end_time")
        # if end_time is not None:
        #     end_time = datetime.strptime(str(end_time), "%Y")

        table = SocioeconomicTable.query.filter_by(id=args.get("table_id")).first()
        if table is None:
            return jsonify(status="fail", data=[], reason="no such table")

        log_id = args.get("log_id")

        if log_id is None:
            old_log = table.get_newest_log()
            log_id = old_log.id

        result = []

        for country_id in args.get("country_ids"):
            for index_id in args.get("index_ids"):
                facts = SocioeconomicFacts.find(table_id=table.id, index_ids=[index_id],
                                                country_ids=[country_id], start_time=int(start_time),
                                                end_time=int(end_time),log_id=log_id)
                index = SocioeconomicIndexes.query.filter_by(id=index_id).first()
                country = Country.query.filter_by(id=country_id).first()
                result.append(
                    {"country":country.to_json(),
                     "index": index.to_json(),
                     "data":[fact.to_json() for fact in facts]})


        # tmp_index = {}
        # tmp_country = {}
        # for fact in facts:
        #     if tmp_index.get(fact.index_id) is None:
        #         tmp_index[fact.index_id] = [fact]
        #     else:
        #         tmp_index[fact.index_id].append(fact)
        #
        # for index_id,same_index_facts in tmp_index.items():
        #
        #     for fact in same_index_facts:
        #         if tmp_country.get(fact.country_id) is None:
        #             tmp_country[fact.country_id] = [fact]
        #         else:
        #             tmp_country[fact.country_id].append(fact)
        #
        #     index = SocioeconomicIndexes.query.filter_by(id=index_id).first()
        #     final_data = []
        #     for country_id, same_country_facts in tmp_country.items():
        #         country = Country.query.filter_by(id=country_id).first()
        #         final_data.append({"country": country.to_json(), "data":[fact.to_json() for fact in same_country_facts]})
        #     result.append({"index":index.to_json(), "data":list(final_data)})

        return jsonify(status="success", reason="", data=result)
    #
    # if request.method == "POST":
    #
    #     if request.args.get("batch") is None:
    #
    #         fact, detail = SocioeconomicFacts.insert_data_with_id(table_id=request.form.get("table_id"),
    #                                                               country_id=request.form.get("country_id"),
    #                                                               time=request.form.get("time"),
    #                                                               index_id=request.form.get("index_id"),
    #                                                               value=request.form.get("value"))
    #         if fact is None:
    #             return jsonify(status="fail", reason=detail, data=[])
    #         Log.log(user_id=current_user.id, target=request.form.get("tablename"), past=str(fact.to_json()),
    #                     note=request.form.get("note",""), pre="")
    #         return jsonify(status="success", reason="", data=[fact.to_json()])
    #
    #     else:
    #         body = request.json
    #         data = body.get("data")
    #
    #         for item in data:
    #
    #             # body:
    #             # {table_id:"", data:[], note: ""}
    #
    #             fact, detail = SocioeconomicFacts.insert_data_with_id(table_id=request.form.get("table_id"),
    #                                                                   country_id=item.get("country_id"),
    #                                                                   time=item.get("time"),
    #                                                                   index_id=item.get("index_id"),
    #                                                                   value=item.get("value"))
    #             if fact is None:
    #                 return jsonify(status="fail", reason="some"+detail, data=[])
    #             Log.log(current_user.id, past=str(fact.to_json()), note=body.get("note",""), target=body.get("table_id"), pre="")
    #         return jsonify(status="success", reason="", data=[])
    #
    # if request.method == "PUT":
    #     body = request.json
    #
    #     for item in body.get("data"):
    #
    #         # body:
    #         # {table_id:"", data:[], note: ""}
    #         pre_fact = SocioeconomicFacts.query.filter_by(id=item.get("id")).first()
    #
    #         fact, detail = SocioeconomicFacts.update_with_id(id=item.get("id"),
    #                                                          country_id=item.get("country_id"),
    #                                                          time=item.get("time"),
    #                                                          index_id=item.get("index_id"),
    #                                                          value=item.get("value"),
    #                                                      )
    #
    #         if fact is None:
    #             return jsonify(status="fail", reason="some" + detail, data=[])
    #
    #         Log.log(current_user.id,
    #                    pre=str(pre_fact.to_json()),
    #                    past=str(fact.to_json()),
    #                    note=body.get("note",""),
    #                    target=body.get("table_id"))
    #
    #     return jsonify(status="success", reason="", data=[])
    #
    # if request.method == "DELETE":
    #
    #     list_str = request.form.get("list")
    #     note = request.form.get("note","")
    #
    #     if list_str is None:
    #         return jsonify(status="fail", reason="list or tablename cant`t be empty", data=[])
    #
    #     fact_ids = json.loads(list_str)
    #     deleted_facts = list()
    #
    #     for id in fact_ids:
    #         fact = SocioeconomicFacts.query.filter_by(id=id).first()
    #         if fact is None:
    #             return jsonify(status="fail", reason="no id :{} fact".format(str(id)), data=[])
    #         deleted_facts.append(fact)
    #
    #     for fact in deleted_facts:
    #         db.session.delete(fact)
    #         db.session.commit()
    #
    #         Log.log(current_user.id, target=fact.index.table.name, past=str(fact.to_json()), note=note )
    #
    #     return jsonify(status="success", reason="", data=[f.to_json() for f in deleted_facts])
    #

@quantify_blueprint.route("/socioeconomic_facts/batch", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_facts_batch():
    if request.method == "POST":
        """
        {
            note:"",
            table_id:,
            data:[{
                country_id:
                time:
                index_id:
                value:
            }]
        }
        """

        body = request.json

        note = body.get("note")
        table_id = body.get("table_id")


        table = SocioeconomicTable.query.filter_by(id=table_id).first()
        if table is None:
            return jsonify(status="fail", reason="no id table", data=[])

        datas = body.get("data")

        old_log = table.get_newest_log()
        new_log = SocLog(note=note, user_id=current_user.id,
                         table_id=table_id, pre_log_id=old_log.id)
        db.session.add(new_log)
        db.session.commit()

        old_facts = SocioeconomicFacts.query.filter(SocioeconomicFacts.log_id == old_log.id).all()
        fields = [i for i in SocioeconomicFacts.__table__.c._data]

        for fact in old_facts:
            f = SocioeconomicFacts()
            for field in fields:
                if field == "log_id":
                    f.log_id = new_log.id
                else:
                    setattr(f, field, getattr(fact, field))
            db.session.add(f)
            db.session.commit()

        for data in datas:
            pre_fact = SocioeconomicFacts.find_one(table_id=table_id, index_id=data.get("index_id"),
                                                   country_id = data.get('country_id'),
                                                   time=data.get('time'), log_id=new_log.id)
            if pre_fact is not None:

                if data.get("value") is not None:
                    # 修改

                    pre_fact.value = data.get("value")
                    pre_fact.time = data.get("time")

                    db.session.add(pre_fact)
                    db.session.commit()
                else:
                    # 删除
                    db.session.delete(pre_fact)
                    db.session.commit()
            else:
                if data.get("value") is not None:
                    # 添加
                    add_fact = SocioeconomicFacts(
                        value=data.get("value"),
                        country_id=data.get("country_id"),
                        time=int(data.get('time')),
                        index_id=data.get("index_id"),
                        log_id=new_log.id
                    )
                    db.session.add(add_fact)
                    db.session.commit()
        table.cur_log_id = new_log.id

        return jsonify(status="success",)





@quantify_blueprint.route("/socioeconomic_table/<id>/indexes", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_facts_indexes(id):
    if request.method == "GET":
        table = SocioeconomicTable.query.filter_by(id=id).first()

        if table is None:
            return jsonify(status="fail", reason="no such id table", data=[])

        return jsonify(status="fail", reason="no such id table", data=[i.to_json() for i in table.indexes])


@quantify_blueprint.route("/socioeconomic_table", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_table():
    if request.method == "GET":
        tables = SocioeconomicTable.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in tables])

    if request.method == "POST":
        table = SocioeconomicTable(name=request.form.get("name"),
                                   cn_alis=request.form.get("cn_alis"),
                                   en_alis=request.form.get("en_alis"))
        db.session.add(table)
        db.session.commit()

        log = SocLog(note="init", table_id=table.id, user_id=current_user.id)
        db.session.add(log)
        db.session.commit()

        table.cur_log_id = log.id
        db.session.add(table)
        db.session.commit()

        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "DELETE":

        table = SocioeconomicTable.query.filter_by(id=request.form.get("id")).first()
        db.session.delete(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "PUT":
        table = SocioeconomicTable.query.filter_by(id=request.form.get("id")).first()
        table.name = request.form.get("name")
        table.cn_alis = request.form.get("cn_alis")
        table.en_alis = request.form.get("en_alis")
        db.session.add(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])


@quantify_blueprint.route("/socioeconomic_index", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_index():
    if request.method == "GET":
        indexes = SocioeconomicIndexes.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in indexes])

    if request.method == "POST":
        index = SocioeconomicIndexes(name=request.form.get("name"),
                                     cn_alis=request.form.get("cn_alis"),
                                     en_alis=request.form.get("en_alis"),
                                     unit=request.form.get("unit"),
                                     table_id=request.form.get("table_id"))
        db.session.add(index)
        db.session.commit()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "PUT":
        index = SocioeconomicIndexes.query.filter_by(id=request.form.get("id")).first()
        index.name = request.form.get("name")
        index.cn_alis = request.form.get("cn_alis")
        index.en_alis = request.form.get("en_alis")
        index.unit = request.form.get("unit")
        db.session.add(index)
        db.session.commit()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "DELETE":

        index = SocioeconomicIndexes.query.filter_by(id=request.form.get("id")).first()
        db.session.delete(index)
        db.session.commit()
        return jsonify(status="success", reason="", data=[index.to_json()])

@quantify_blueprint.route("/socioeconomic_facts/graph", methods=['GET', 'POST','PUT', 'DELETE'])
def socioeconomic_facts_graph():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = std_json(request.args)

        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        table = SocioeconomicTable.query.filter_by(id=args.get("table_id")).first()
        if table is None:
            return jsonify(status="fail", data=[], reason="no such table")

        log_id = args.get("log_id")

        if log_id is None:
            old_log = table.get_newest_log()
            log_id = old_log.id

        start_time = args.get("start_time")
        # if start_time is not None:
        #     start_time = datetime.strptime(str(start_time), "%Y")

        end_time = args.get("end_time")
        # if end_time is not None:
        #     end_time = datetime.strptime(str(end_time), "%Y")
        datas = []
        for index_id in args.get('index_ids'):
            index = SocioeconomicIndexes.query.filter_by(id=index_id).first()
            data = {'index':index.to_json()}
            series = []
            for country_id in args.get('country_ids'):
                facts=SocioeconomicFacts.find(table_id=args.get("table_id"), index_ids=[index_id],
                                        country_ids=[country_id], start_time=int(start_time),
                                        end_time=int(end_time), log_id=log_id)
                country = Country.query.filter_by(id=country_id).first()
                serie = {'country':country.to_json()}
                fact_series = []
                for fact in facts:
                    fact_serie = {'x':fact.time, 'y':fact.value}
                    fact_series.append(fact_serie)
                serie['series'] = fact_series
                series.append(serie)
            data['series'] = series
            datas.append(data)
        return jsonify({
            'status': 'success',
            'reason': '',
            'data': datas
        })
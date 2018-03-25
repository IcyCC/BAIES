from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify import Country
from app.model.comm.log import ArgLog
from app.model.quantify.agriculture_products import AgricultureIndexes, AgricultureKind, AgricultureFacts, \
    AgricultureTable
from app.model.user import Permission
from flask_login import current_user
from app import std_json
import json
import sqlalchemy
from datetime import datetime
from sqlalchemy.exc import IntegrityError
import pandas

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
    "log_id",
    "kind_ids"
)


def check_args(father, son):
    return set(father) > set(son)


def find_in_list(items, id, func):
    for item in items:
        if func(item, id):
            return item

    return None


@quantify_blueprint.route("/agriculture_facts", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_facts():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = std_json(request.args)

        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        start_time = args.get('start_time')
        end_time = args.get('end_time')

        table = AgricultureTable.query.filter_by(id=args.get('table_id')).first()
        if table is None:
            return jsonify(status="fail", data=[], reason="no such table")

        log_id = args.get('log_id')
        if log_id is None:
            log_id = table.cur_log_id

        result = []
        for country_id in args.get("country_ids"):
            for index_id in args.get("index_ids"):
                for kind_id in args.get('kind_ids'):
                    facts = AgricultureFacts.find(table_id=table.id, index_ids=[index_id], kind_ids=[kind_id],
                                                  country_ids=[country_id], start_time=int(start_time),
                                                  end_time=int(end_time), log_id=log_id)
                    index = AgricultureIndexes.query.filter_by(id=index_id).first()
                    country = Country.query.filter_by(id=country_id).first()
                    kind = AgricultureKind.query.filter_by(id=kind_id).first()
                    result.append(
                        {"country": country.to_json(),
                         "index": index.to_json(),
                         "kind": kind.to_json(),
                         "data": [fact.to_json() for fact in facts]})

        # facts = AgricultureFacts.find(table_id=args.get("table_id"), index=args.get("index"),
        #                                   country=args.get("country"), start_time=args.get("start_time"))
        #
        # result = list()
        #
        # for fact in facts:
        #     _tmp_has_index = find_in_list(result, fact.index_id, lambda x, y: x.get("index_id") == y)
        #     if _tmp_has_index is None:
        #         result.append({"index_id": fact.index_id,
        #                        "data": [{"country_id": fact.country_id,
        #                                  "data": [fact.to_json()]}]})
        #     else:
        #         _tmp_has_country = find_in_list(result, fact.country_id, lambda x, y: x.get("country_id") == y)
        #         if _tmp_has_country is None:
        #             _tmp_has_index['data'].append({"country_id": fact.country_id,
        #                                            "data": [fact.to_json()]})
        #         else:
        #             _tmp_has_country["data"].append(fact.to_json)

        return jsonify(status="success", reason="", data=result)

    # if request.method == "POST":
    #
    #     if request.args.get("batch") is None:
    #
    #         fact, detail = AgricultureFacts.insert_data_with_id(table_id=request.form.get("table_id"),
    #                                                             country_id=request.form.get("country_id"),
    #                                                             time=request.form.get("time"),
    #                                                             index_id=request.form.get("index_id"),
    #                                                             kind_id=request.form.get("kind_id"),
    #                                                             value=request.form.get("value"))
    #
    #         if fact is None:
    #             return jsonify(status="fail", reason=detail, data=[])
    #         PostLog.log(user_id=current_user.id, target=request.form.get("tablename"), detail=str(fact.to_json()),
    #                     note=request.form.get("note",""))
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
    #             fact, detail = AgricultureFacts.insert_data_with_id(table_id=request.form.get("table_id"),
    #                                                                 country_id=item.get("country_id"),
    #                                                                 time=item.get("time"),
    #                                                                 index_id=item.get("index_id"),
    #                                                                 kind_id=item.get("kind_id"),
    #                                                                 value=item.get("value"))
    #             if fact is None:
    #                 return jsonify(status="fail", reason="some"+detail, data=[])
    #             PostLog.log(current_user.id, detail=str(fact.to_json()), note=body.get("note",""), target=body.get("table_id"))
    #         return jsonify(status="success", reason="", data=[])
    #
    # if request.method == "PUT":
    #     body = request.json
    #
    #     for item in body.get("data"):
    #
    #         # body:
    #         # {table_id:"", data:[], note: ""}
    #         pre_fact = AgricultureFacts.query.filter_by(id=item.get("id")).first()
    #
    #         fact, detail = AgricultureFacts.update_with_id(id=item.get("id"),
    #                                                        country_id=item.get("country_id"),
    #                                                        time=item.get("time"),
    #                                                        index_id=item.get("index_id"),
    #                                                        value=item.get("value"),
    #                                                        kind_id=item.get("kind_id"))
    #
    #         if fact is None:
    #             return jsonify(status="fail", reason="some" + detail, data=[])
    #         PutLog.log(current_user.id, pre=str(pre_fact.to_json()), past=str(fact.to_json()), note=body.get("note",""),
    #                    target=body.get("table_id"))
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
    #         fact = AgricultureFacts.query.filter_by(id=id).first()
    #         if fact is None:
    #             return jsonify(status="fail", reason="no id :{} fact".format(str(id)), data=[])
    #         deleted_facts.append(fact)
    #
    #     for fact in deleted_facts:
    #         db.session.delete(fact)
    #         db.session.commit()
    #
    #         DeleteLog.log(current_user.id, target=fact.index.table.name, detail=str(fact.to_json()),note=note)
    #
    #     return jsonify(status="success", reason="", data=[f.to_json() for f in deleted_facts])


@quantify_blueprint.route("/agriculture_facts/batch", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_facts_batch():
    if request.method == "POST":
        """
        {
            note:"",
            table_id:,
            data:[{
                country_id:
                time:
                index_id:
                kind_id:
                value:
            }]
        }
        """

        body = request.json

        note = body.get("note")
        table_id = body.get("table_id")

        table = AgricultureTable.query.filter_by(id=table_id).first()
        if table is None:
            return jsonify(status="fail", reason="no id table", data=[])

        datas = body.get("data")

        old_log = table.cur_log
        new_log = ArgLog(note=note, user_id=current_user.id,
                         table_id=table_id, timestamp=datetime.now(),pre_log_id=old_log.id)
        db.session.add(new_log)
        db.session.commit()

        old_facts = AgricultureFacts.query.filter(AgricultureFacts.log_id == old_log.id).all()
        fields = [i for i in AgricultureFacts.__table__.c._data]

        for fact in old_facts:
            f = AgricultureFacts()
            for field in fields:
                if field == "id":
                    print("change id")
                elif field == "log_id":
                    f.log_id = new_log.id
                elif field == "time_stamp":
                    f.time_stamp = datetime.now()
                else:
                    setattr(f, field, getattr(fact, field))
            db.session.add(f)
            db.session.commit()

        for data in datas:
            pre_fact = AgricultureFacts.find_one(table_id=table_id, index_id=data.get("index_id"),
                                                 country_id=data.get('country_id'), kind_id=data.get('kind_id'),
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
                    add_fact = AgricultureFacts(
                        value=data.get("value"),
                        country_id=data.get("country_id"),
                        time=int(data.get('time')),
                        index_id=data.get("index_id"),
                        kind_id=data.get("kind_id"),
                        log_id=new_log.id
                    )
                    db.session.add(add_fact)
                    db.session.commit()
        table.cur_log_id = new_log.id
        db.session.add(table)
        db.session.commit()

        return jsonify(status="success", )


@quantify_blueprint.route("/agriculture_table/<id>/indexes", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_facts_indexes(id):
    if request.method == "GET":
        table = AgricultureTable.query.filter_by(id=id).first()

        if table is None:
            return jsonify(status="fail", reason="no such id table", data=[])

        return jsonify(status="fail", reason="no such id table", data=[i.to_json() for i in table.indexes])


@quantify_blueprint.route("/agriculture_table", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_table():
    if request.method == "GET":
        tables = AgricultureTable.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in tables])

    if request.method == "POST":
        table = AgricultureTable(name=request.form.get("name"),
                                 cn_alis=request.form.get("cn_alis"),
                                 en_alis=request.form.get("en_alis"))
        db.session.add(table)
        db.session.commit()

        log = ArgLog(note="init", table_id=table.id, user_id=current_user.id)
        db.session.add(log)
        db.session.commit()

        table.cur_log_id = log.id
        db.session.add(table)
        db.session.commit()

        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "DELETE":
        table = AgricultureTable.query.filter_by(id=request.form.get("id")).first()
        db.session.delete(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])

    if request.method == "PUT":
        table = AgricultureTable.query.filter_by(id=request.form.get("id")).first()
        for k, v in request.form.items():
            if hasattr(table, k):
                setattr(table, k, v)
        db.session.add(table)
        db.session.commit()
        return jsonify(status="success", reason="", data=[table.to_json()])


@quantify_blueprint.route("/agriculture_index", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_index():
    if request.method == "GET":
        indexes = AgricultureIndexes.query.all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in indexes])

    if request.method == "POST":
        index = AgricultureIndexes(name=request.form.get("name"),
                                   cn_alis=request.form.get("cn_alis"),
                                   en_alis=request.form.get("en_alis"),
                                   unit=request.form.get("unit"),
                                   table_id=request.form.get("table_id"))
        db.session.add(index)
        db.session.commit()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "PUT":
        index = AgricultureIndexes.query.filter_by(id=request.form.get("id")).first()
        for k, v in request.form.items():
            if hasattr(index, k):
                setattr(index, k, v)
        db.session.add(index)
        db.session.commit()

        return jsonify(status="success", reason="", data=[index.to_json()])

    if request.method == "DELETE":
        index = AgricultureIndexes.query.filter_by(id=request.form.get("id")).first()
        db.session.delete(index)
        db.session.commit()
        return jsonify(status="success", reason="", data=[index.to_json()])


@quantify_blueprint.route("/agriculture_kinds", methods=['GET', 'POST', 'DELETE'])
def agriculture_kinds():
    if request.method == "GET":
        kinds = AgricultureKind.query.all()
        return jsonify(status="success", reason="", data=[t.to_json_by_fact() for t in kinds])

    if request.method == "POST":
        kind = AgricultureKind(name=request.form.get("name"),
                               cn_alis=request.form.get("cn_alis"),
                               en_alis=request.form.get("en_alis"))
        db.session.add(kind)
        db.session.commit()
        return jsonify(status="success", reason="", data=[kind.to_json_by_fact()])

    if request.method == "DELETE":
        kind = AgricultureKind.filter_by(id=request.args.get("id")).first()
        db.session.delete(kind)
        db.session.commit()
        return jsonify(status="success", reason="", data=[kind.to_json_by_fact()])

    if request.method == "PUT":
        kind = AgricultureKind.query.filter_by(id=request.form.get("id")).first()
        for k, v in request.form.items():
            if hasattr(kind, k):
                setattr(kind, k, v)
        db.session.add(kind)
        db.session.commit()
        return jsonify(status="success", reason="", data=[kind.to_json_by_fact()])


@quantify_blueprint.route("/agriculture_facts/graph", methods=['GET', 'POST', 'PUT', 'DELETE'])
def agriculture_facts_graph():
    if request.method == "GET":

        # if not current_user.can(Permission.QUANTIFY_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        args = std_json(request.args)

        if not check_args(ALLOW_ARGS, args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        table = AgricultureTable.query.filter_by(id=args.get("table_id")).first()
        if table is None:
            return jsonify(status="fail", data=[], reason="no such table")

        log_id = args.get("log_id")

        if log_id is None:
            old_log = table.cur_log
            log_id = old_log.id

        start_time = args.get("start_time")
        # if start_time is not None:
        #     start_time = datetime.strptime(str(start_time), "%Y")

        end_time = args.get("end_time")
        # if end_time is not None:
        #     end_time = datetime.strptime(str(end_time), "%Y")
        datas = []
        for index_id in args.get("index_ids"):
            for country_id in args.get("country_ids"):
                for kind_id in args.get("kind_ids"):
                    index = AgricultureIndexes.query.filter_by(id=index_id).first()
                    kind = AgricultureKind.query.filter_by(id=kind_id).first()
                    country = Country.query.filter_by(id=country_id).first()
                    facts = AgricultureFacts.find(table_id=args.get("table_id"), index_ids=[index_id], kind_ids=[kind_id],
                                                  country_ids=[country_id], start_time=int(start_time),
                                                  end_time=int(end_time), log_id=log_id)
                    fact_series = []
                    for fact in facts:
                        fact_serie = {'x': fact.time, 'y': fact.value}
                        fact_series.append(fact_serie)
                    data = {
                        'index': index.to_json_by_fact(),
                        'kind': kind.to_json_by_fact(),
                        'country': country.to_json(),
                        'series': fact_series
                    }
                    datas.append(data)
        return jsonify({
            'status': 'success',
            'reason': '',
            'data': datas
        })

@quantify_blueprint.route('/agriculture_excel', methods=['POST'])
def agriculture_excel():
    if 'filename' in request.json:
        filename = current_app.config['UPLOAD_FOLDER']+'/'+request.json['filename']
        df = pandas.read_excel(filename)
    else:
        return jsonify({
            'status':'fail',
            'reason':'there is no filename'
        })

    if 'table_id' in request.json:
        table_id = request.json['table_id']
        table = AgricultureTable.query.filter_by(id=table_id).first()
        if table is None:
            return jsonify({
                'status':'fail',
                'reason':'the table does not exist'
            })
    else:
        return jsonify({
            'status':'fail',
            'reason':'there is no table id'
        })

    if 'field' in request.json:
        field = request.json['field']
    else:
        return jsonify({
            'status':'fail',
            'reason':'there is no field'
        })

    table_id = request.json['table_id']
    years = []

    note = request.json['note']
    old_log = table.cur_log
    new_log = ArgLog(note=note, user_id=current_user.id,
                     table_id=table_id, pre_log_id=old_log.id, timestamp=datetime.now())
    db.session.add(new_log)
    try:

        db.session.commit()
    except IntegrityError:
        print("EXCEPETION")
        print(1)
        db.session.rollback()
    table.cur_log_id = new_log.id
    db.session.add(table)
    try:
        db.session.commit()
    except IntegrityError:
        print("EXCEPETION")
        db.session.rollback()
    log_id = table.cur_log_id
    for item in df.head(0):
        if item not in ['Country', 'Indicator', 'Product']:
            years.append(item)
    print(years)
    for i in range(0, (int)(df.size / len(df.columns))):
        country_l = getattr(Country, field.strip())
        country_name = df.iloc[i]['Country']
        country = Country.query.filter(country_l==country_name).first()
        country_id = country.id
        index_l = getattr(AgricultureIndexes, field.strip())
        index_name = df.iloc[i]['Indicator']
        index = AgricultureIndexes.query.filter(AgricultureIndexes.table_id==table_id).filter(index_l==index_name).first()
        index_id = index.id
        kind_l = getattr(AgricultureKind, field.strip())
        kind_name = df.iloc[i]['Product']
        kind = AgricultureKind.query.filter(kind_l==kind_name).first()
        kind_id = kind.id
        for year in years:
            value = df.iloc[i][year]
            print(year)
            if value != 'undefined':
                fact = AgricultureFacts(time=int(year), index_id=index_id, country_id=country_id, value=int(value), log_id=log_id, kind_id=kind_id)
                db.session.add(fact)
                try:
                    db.session.commit()
                except IntegrityError:
                    print("EXCEPETION")
                    db.session.rollback()

            db.session.commit()
    return jsonify({
        'status':'success',
        'reason':''
    })

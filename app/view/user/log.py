from flask import request, jsonify, current_app
from app import db
from . import user_blueprint
from app.model.user import *
from app.model.comm.log import *
from app import check_args,std_json
from flask_login import current_user,login_user, logout_user,login_required
import sqlalchemy

@user_blueprint.route("/SocLog" , methods=['GET', 'POST'])
def put_logs():

    fields = [i for i in SocLog.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)
        args = std_json(request.args)
        query = SocLog.query

        for k, v in args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        query = query.order_by(SocLog.id.desc())

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json_simple() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                       )

    if request.method == "POST":

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = SocLog()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/SocLog/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def put_logs_r(q_id):

    c = SocLog.query.filter_by(id=q_id).first()
    fields = [i for i in SocLog.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":
        #
        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        # if not current_user.can(Permission.QUANTIFY_W):
        #     return jsonify(status="fail", data=[], reason="no permission")


        try:
            db.session.delete(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/ArgLog" , methods=['GET', 'POST'])
def put_logs_arg():

    fields = [i for i in ArgLog.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)
        args = std_json(request.args)
        query = ArgLog.query

        for k, v in args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        query = query.order_by(ArgLog.id.desc())

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json_simple() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                       )

    if request.method == "POST":

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ArgLog()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/ArgLog/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def put_logs_r_arg(q_id):

    c = ArgLog.query.filter_by(id=q_id).first()
    fields = [i for i in ArgLog.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":
        #
        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        # if not current_user.can(Permission.QUANTIFY_W):
        #     return jsonify(status="fail", data=[], reason="no permission")


        try:
            db.session.delete(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


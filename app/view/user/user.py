from flask import request, jsonify, current_app
from app import db
from . import user_blueprint
from app.model.user import *
from app import check_args
from flask_login import current_user,login_user, logout_user,login_required
import sqlalchemy



@user_blueprint.route("/User" , methods=['GET', 'POST'])
def users():

    fields = [i for i in User.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.USER_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = User.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.USER_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = User()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        c.password = form.get("password")

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/User/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def users_r(q_id):

    c = User.query.filter_by(id=q_id).first()
    fields = [i for i in User.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.USER_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.USER_W):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        c.password = form.get("password")

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")


        try:
            db.session.delete(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/Role" , methods=['GET', 'POST'])
def roles():

    fields = [i for i in Role.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.USER_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = Role.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.USER_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = Role()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/Role/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def roles_r(q_id):

    c = Role.query.filter_by(id=q_id).first()
    fields = [i for i in Role.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.USER_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.USER_W):
            return jsonify(status="fail", data=[], reason="no permission")

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

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")


        try:
            db.session.delete(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


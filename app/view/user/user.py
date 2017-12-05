from flask import request, jsonify, current_app
from app import db
from . import user_blueprint
from app.model.user import *
from app import check_args
from flask_login import current_user,login_user, logout_user,login_required


@user_blueprint.route("/User" , methods=['GET', 'POST'])
def users():
    if request.method == "GET":
        if not check_args(dir(User), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = User.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":
        form = request.form
        if not check_args(dir(User), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = User()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        c.password = request.form.get("password")

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/User/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  users_r(q_id):

    c = User.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":
        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not check_args(dir(User), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        db.session.delete(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/Role" , methods=['GET', 'POST'])
def roles():
    if request.method == "GET":
        if not check_args(dir(Role), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = Role.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":
        form = request.form
        if not check_args(dir(Role), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = Role()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@user_blueprint.route("/Role/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  roles_r(q_id):

    c = Role.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":
        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not check_args(dir(Role), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        db.session.delete(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


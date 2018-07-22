from flask import request, jsonify, current_app
from app import db
from . import qualitative_blueprint
from app.model.qualitative.information import *
from app import check_args,SPECIAL_ARGS, std_json
from app.model.user import Permission
from flask_login import current_user
import sqlalchemy



@qualitative_blueprint.route("/Post" , methods=['GET', 'POST'])
def post():

    fields = [i for i in Post.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = Post.query
        args = std_json(request.args)
        for k, v in args.items():
            if k in fields:
                query = query.filter_by(**{k: v})
        query = query.order_by(Post.timestamp.desc())

        # pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        #                                             error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in query],
                       # page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                       )

    if request.method == "POST":

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = Post()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)
        c.user_id = current_user.id
        c.show = False

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@qualitative_blueprint.route("/Post/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def post_r(q_id):

    c = Post.query.filter_by(id=q_id).first()
    fields = [i for i in Post.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

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

@qualitative_blueprint.route("/Post/simple" , methods=['GET', 'POST'])
def post_simple():

    fields = [i for i in Post.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = Post.query
        args = std_json(request.args)
        for k, v in args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        query = query.order_by(Post.timestamp.desc()).limit(40)

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json_simple() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                       )

@qualitative_blueprint.route("/Kind" , methods=['GET', 'POST'])
def kind():

    fields = [i for i in Kind.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = Kind.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        # pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        #                                             error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in query],
                       # page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                    )

    if request.method == "POST":

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = Kind()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@qualitative_blueprint.route("/Images" , methods=['GET', 'POST'])
def images():

    fields = [i for i in Image.__table__.c._data]

    if request.method == "GET":

        # if not current_user.can(Permission.QUALITATIVE_R):
        #     return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = Image.query
        args = std_json(request.args)
        for k, v in args.items():
            if k in fields:
                query = query.filter_by(**{k: v})
        query = query.order_by(Image.id.desc())

        # pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
        #                                             error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in query],
                       # page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total}
                       )

    if request.method == "POST":

        # if not current_user.can(Permission.QUALITATIVE_W):
        #     return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = Image()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)
        c.user_id = current_user.id
        c.show = False

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@qualitative_blueprint.route("/Images/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def images_r(q_id):

    c = Image.query.filter_by(id=q_id).first()
    fields = [i for i in Image.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

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

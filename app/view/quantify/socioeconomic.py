from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify.socioeconomic import *
from app import check_args
from app.model.user import permission_required,Permission


@quantify_blueprint.route("/CountryProfiles" , methods=['GET', 'POST'])
def country_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(CountryProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = CountryProfiles.query

        for k, v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":
        permission_required(Permission.QUANTIFY_W)
        form = request.form
        if not check_args(dir(CountryProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = CountryProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/CountryProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def country_profiles_r(q_id):

    c = CountryProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":
        permission_required(Permission.QUANTIFY_R)
        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(CountryProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "DELETE":

        permission_required(Permission.QUANTIFY_W)

        db.session.delete(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])

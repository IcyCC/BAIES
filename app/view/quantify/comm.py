from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify import Country
from app.model.user import Permission
from flask_login import current_user
from app.model.comm.log import SocLog
import sqlalchemy

@quantify_blueprint.route("/country", methods=['GET', 'POST'])
def route_country():

    if request.method == "GET":
        country = Country.r_query().all()
        return jsonify(status="success", reason="", data=[t.to_json() for t in country])

    if request.method == "POST":
        country = Country(name=request.form.get("name"),
                          cn_alias=request.form.get("cn_alis"),
                          en_alias=request.form.get("en_alis"))
        db.session.add(country)
        db.session.commit()
        return jsonify(status="success", reason="", data=[country.to_json()])

    if request.method == "DELETE":
        country = Country.query.filter_by(id=request.args.get("id")).first()
        db.session.delete(country)
        db.session.commit()
        return jsonify(status="success", reason="", data=[country.to_json()])


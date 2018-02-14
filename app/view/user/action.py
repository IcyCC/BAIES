import os
from flask import request, jsonify, current_app,url_for
from app import db
from . import user_blueprint
from app.model.user import *
from app import check_args
from flask_login import current_user,login_user, logout_user,login_required
from werkzeug.utils import secure_filename
from BAIES import app



@user_blueprint.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()

        if user is None or not user.verify_password(password=password):
            return jsonify(status="fail", reason="no this user or password error", data=[])

        login_user(user, remember=False)

        return jsonify(status="success", reason="", data=[user.to_json()])

    if request.method == "GET":
        return "<html><head>" \
               "<title></title></head>" \
               "<body>" \
               "<form action=\"/user/login\" method=\"post\">" \
               "用户名:<input type=\"text\" name=\"username\">" \
               "密码:<input type=\"password\" name=\"password\">" \
               "<input type=\"submit\" value=\"登陆\"></form></body></html>"


@user_blueprint.route("/logout", methods=["GET"])
@login_required
def logout():
    if request.method == "GET":
        logout_user()
        return jsonify(status="success", reason="", data=[])

@user_blueprint.route("/current_user",methods=["GET"])
def get_current():

    return jsonify(status="success", reason="", data=[current_user.to_json()])

@user_blueprint.route("/upload", methods=["POST"])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify(status="success", reason="", data=url_for("static",filename="upload/"+filename))
        return jsonify(status="fail", reason="Unknow", data="")


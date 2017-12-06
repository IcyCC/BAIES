from flask import request, jsonify, current_app
from app import db
from . import quantify_blueprint
from app.model.quantify.agriculture_products import *
from app import check_args,SPECIAL_ARGS
from app.model.user import Permission
from flask_login import current_user
import sqlalchemy


@quantify_blueprint.route("/AgriculturalProductionValueProfiles" , methods=['GET', 'POST'])
def agricultural_production_value_profiles():

    fields = [i for i in AgriculturalProductionValueProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgriculturalProductionValueProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgriculturalProductionValueProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgriculturalProductionValueProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agricultural_production_value_profiles_r(q_id):

    c = AgriculturalProductionValueProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in AgriculturalProductionValueProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgriculturalProductionProfiles" , methods=['GET', 'POST'])
def agricultural_production_profiles():

    fields = [i for i in AgriculturalProductionProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgriculturalProductionProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgriculturalProductionProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgriculturalProductionProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agricultural_production_profiles_r(q_id):

    c = AgriculturalProductionProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in AgriculturalProductionProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/GrainProductionProfiles" , methods=['GET', 'POST'])
def grain_production_profiles():

    fields = [i for i in GrainProductionProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = GrainProductionProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = GrainProductionProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/GrainProductionProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def grain_production_profiles_r(q_id):

    c = GrainProductionProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in GrainProductionProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/OtherCropProductionProfiles" , methods=['GET', 'POST'])
def other_crop_production_profiles():

    fields = [i for i in OtherCropProductionProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = OtherCropProductionProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = OtherCropProductionProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/OtherCropProductionProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def other_crop_production_profiles_r(q_id):

    c = OtherCropProductionProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in OtherCropProductionProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/MeatProductionProfiles" , methods=['GET', 'POST'])
def meat_production_profiles():

    fields = [i for i in MeatProductionProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = MeatProductionProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = MeatProductionProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/MeatProductionProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def meat_production_profiles_r(q_id):

    c = MeatProductionProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in MeatProductionProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AnimalHusbandryProfiles" , methods=['GET', 'POST'])
def animal_husbandry_profiles():

    fields = [i for i in AnimalHusbandryProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AnimalHusbandryProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AnimalHusbandryProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AnimalHusbandryProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def animal_husbandry_profiles_r(q_id):

    c = AnimalHusbandryProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in AnimalHusbandryProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AquaticProductsProfiles" , methods=['GET', 'POST'])
def aquatic_products_profiles():

    fields = [i for i in AquaticProductsProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AquaticProductsProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AquaticProductsProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AquaticProductsProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def aquatic_products_profiles_r(q_id):

    c = AquaticProductsProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in AquaticProductsProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/PlantProfiles" , methods=['GET', 'POST'])
def plant_profiles():

    fields = [i for i in PlantProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = PlantProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = PlantProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/PlantProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def plant_profiles_r(q_id):

    c = PlantProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in PlantProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AnimalHusbandryAquaticProducts" , methods=['GET', 'POST'])
def animal_husbandry_aquatic_products():

    fields = [i for i in AnimalHusbandryAquaticProducts.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AnimalHusbandryAquaticProducts.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AnimalHusbandryAquaticProducts()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AnimalHusbandryAquaticProducts/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def animal_husbandry_aquatic_products_r(q_id):

    c = AnimalHusbandryAquaticProducts.query.filter_by(id=q_id).first()
    fields = [i for i in AnimalHusbandryAquaticProducts.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgriculturalProductsTradeProfiles" , methods=['GET', 'POST'])
def agricultural_products_trade_profiles():

    fields = [i for i in AgriculturalProductsTradeProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgriculturalProductsTradeProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgriculturalProductsTradeProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgriculturalProductsTradeProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agricultural_products_trade_profiles_r(q_id):

    c = AgriculturalProductsTradeProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in AgriculturalProductsTradeProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/KindAgriculturalProductsTradeMoneyProfiles" , methods=['GET', 'POST'])
def kind_agricultural_products_trade_money_profiles():

    fields = [i for i in KindAgriculturalProductsTradeMoneyProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = KindAgriculturalProductsTradeMoneyProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = KindAgriculturalProductsTradeMoneyProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/KindAgriculturalProductsTradeMoneyProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def kind_agricultural_products_trade_money_profiles_r(q_id):

    c = KindAgriculturalProductsTradeMoneyProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in KindAgriculturalProductsTradeMoneyProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/KindAgriculturalProductsTradeNumProfiles" , methods=['GET', 'POST'])
def kind_agricultural_products_num_money_profiles():

    fields = [i for i in KindAgriculturalProductsTradeNumProfiles.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = KindAgriculturalProductsTradeNumProfiles.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = KindAgriculturalProductsTradeNumProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/KindAgriculturalProductsTradeNumProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def kind_agricultural_products_num_money_profiles_r(q_id):

    c = KindAgriculturalProductsTradeNumProfiles.query.filter_by(id=q_id).first()
    fields = [i for i in KindAgriculturalProductsTradeNumProfiles.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgricultureForeignInvestmentStock" , methods=['GET', 'POST'])
def agriculture_foreign_investment_stock():

    fields = [i for i in AgricultureForeignInvestmentStock.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgricultureForeignInvestmentStock.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureForeignInvestmentStock()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureForeignInvestmentStock/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agriculture_foreign_investment_stock_r(q_id):

    c = AgricultureForeignInvestmentStock.query.filter_by(id=q_id).first()
    fields = [i for i in AgricultureForeignInvestmentStock.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgricultureForeignInvestmentStockStructure" , methods=['GET', 'POST'])
def agriculture_foreign_investment_stock_structure():

    fields = [i for i in AgricultureForeignInvestmentStockStructure.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgricultureForeignInvestmentStockStructure.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureForeignInvestmentStockStructure()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureForeignInvestmentStockStructure/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agriculture_foreign_investment_stock_structure_r(q_id):

    c = AgricultureForeignInvestmentStockStructure.query.filter_by(id=q_id).first()
    fields = [i for i in AgricultureForeignInvestmentStockStructure.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgricultureForeignInvestmentFluent" , methods=['GET', 'POST'])
def agriculture_foreign_investment_fluent():

    fields = [i for i in AgricultureForeignInvestmentFluent.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgricultureForeignInvestmentFluent.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureForeignInvestmentFluent()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureForeignInvestmentFluent/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agriculture_foreign_investment_fluent_r(q_id):

    c = AgricultureForeignInvestmentFluent.query.filter_by(id=q_id).first()
    fields = [i for i in AgricultureForeignInvestmentFluent.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgricultureForeignInvestmentImport" , methods=['GET', 'POST'])
def agriculture_foreign_investment_import():

    fields = [i for i in AgricultureForeignInvestmentImport.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgricultureForeignInvestmentImport.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureForeignInvestmentImport()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureForeignInvestmentImport/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agriculture_foreign_investment_import_r(q_id):

    c = AgricultureForeignInvestmentImport.query.filter_by(id=q_id).first()
    fields = [i for i in AgricultureForeignInvestmentImport.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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



@quantify_blueprint.route("/AgricultureForeignInvestmentUsedStructure" , methods=['GET', 'POST'])
def agriculture_foreign_investment_used_structure():

    fields = [i for i in AgricultureForeignInvestmentUsedStructure.__table__.c._data]

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        if not check_args(fields, request.args.keys()):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        page = int(page)

        query = AgricultureForeignInvestmentUsedStructure.query

        for k, v in request.args.items():
            if k in fields:
                query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        if not current_user.can(Permission.QUANTIFY_W):
            return jsonify(status="fail", data=[], reason="no permission")

        form = request.form
        if not check_args(fields, form.keys()):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureForeignInvestmentUsedStructure()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        try:
            db.session.add(c)
            db.session.commit()
        except sqlalchemy.exc.OperationalError as e:
            return jsonify(status="fail", reason=e, data=[])

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureForeignInvestmentUsedStructure/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def agriculture_foreign_investment_used_structure_r(q_id):

    c = AgricultureForeignInvestmentUsedStructure.query.filter_by(id=q_id).first()
    fields = [i for i in AgricultureForeignInvestmentUsedStructure.__table__.c._data]


    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        if not current_user.can(Permission.QUANTIFY_R):
            return jsonify(status="fail", data=[], reason="no permission")

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        if not current_user.can(Permission.QUANTIFY_W):
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


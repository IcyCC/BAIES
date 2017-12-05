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

        for k,v in request.args.items():
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
def  country_profiles_r(q_id):

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



@quantify_blueprint.route("/PopulationProfiles" , methods=['GET', 'POST'])
def population_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(PopulationProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = PopulationProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(PopulationProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = PopulationProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/PopulationProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  population_profiles_r(q_id):

    c = PopulationProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(PopulationProfiles), request.args):
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



@quantify_blueprint.route("/SexDistributionProfiles" , methods=['GET', 'POST'])
def sex_distribution_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(SexDistributionProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = SexDistributionProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(SexDistributionProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = SexDistributionProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/SexDistributionProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  sex_distribution_profiles_r(q_id):

    c = SexDistributionProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(SexDistributionProfiles), request.args):
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



@quantify_blueprint.route("/LaborPopulationProfiles" , methods=['GET', 'POST'])
def labor_population_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(LaborPopulationProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = LaborPopulationProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(LaborPopulationProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = LaborPopulationProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/LaborPopulationProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  labor_population_profiles_r(q_id):

    c = LaborPopulationProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(LaborPopulationProfiles), request.args):
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



@quantify_blueprint.route("/EconomicProfiles" , methods=['GET', 'POST'])
def economic_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(EconomicProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = EconomicProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(EconomicProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = EconomicProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/EconomicProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  economic_profiles_r(q_id):

    c = EconomicProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(EconomicProfiles), request.args):
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



@quantify_blueprint.route("/EconomicIndexProfiles" , methods=['GET', 'POST'])
def economic_index_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(EconomicIndexProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = EconomicIndexProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(EconomicIndexProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = EconomicIndexProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/EconomicIndexProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  economic_index_profiles_r(q_id):

    c = EconomicIndexProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(EconomicIndexProfiles), request.args):
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



@quantify_blueprint.route("/LivingStandardOfResidents" , methods=['GET', 'POST'])
def living_standard_of_residents():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(LivingStandardOfResidents), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = LivingStandardOfResidents.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(LivingStandardOfResidents), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = LivingStandardOfResidents()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/LivingStandardOfResidents/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  living_standard_of_residents_r(q_id):

    c = LivingStandardOfResidents.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(LivingStandardOfResidents), request.args):
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



@quantify_blueprint.route("/ConsumerSpendingResidents" , methods=['GET', 'POST'])
def consumer_spending_residents():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ConsumerSpendingResidents), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ConsumerSpendingResidents.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ConsumerSpendingResidents), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ConsumerSpendingResidents()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ConsumerSpendingResidents/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  consumer_spending_residents_r(q_id):

    c = ConsumerSpendingResidents.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ConsumerSpendingResidents), request.args):
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



@quantify_blueprint.route("/TradeProfiles" , methods=['GET', 'POST'])
def trade_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(TradeProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = TradeProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(TradeProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = TradeProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/TradeProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  trade_profiles_r(q_id):

    c = TradeProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(TradeProfiles), request.args):
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



@quantify_blueprint.route("/ReserveProfiles" , methods=['GET', 'POST'])
def reserve_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ReserveProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ReserveProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ReserveProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ReserveProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ReserveProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  reserve_profiles_r(q_id):

    c = ReserveProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ReserveProfiles), request.args):
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



@quantify_blueprint.route("/LoanProfiles" , methods=['GET', 'POST'])
def loan_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(LoanProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = LoanProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(LoanProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = LoanProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/LoanProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  loan_profiles_r(q_id):

    c = LoanProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(LoanProfiles), request.args):
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



@quantify_blueprint.route("/HealthyProfiles" , methods=['GET', 'POST'])
def healthy_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(HealthyProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = HealthyProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(HealthyProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = HealthyProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/HealthyProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  healthy_profiles_r(q_id):

    c = HealthyProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(HealthyProfiles), request.args):
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



@quantify_blueprint.route("/BirthDeathRate" , methods=['GET', 'POST'])
def birth_death_rate():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(BirthDeathRate), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = BirthDeathRate.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(BirthDeathRate), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = BirthDeathRate()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/BirthDeathRate/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  birth_death_rate_r(q_id):

    c = BirthDeathRate.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(BirthDeathRate), request.args):
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



@quantify_blueprint.route("/BirthProfiles" , methods=['GET', 'POST'])
def birth_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(BirthProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = BirthProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(BirthProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = BirthProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/BirthProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  birth_profiles_r(q_id):

    c = BirthProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(BirthProfiles), request.args):
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



@quantify_blueprint.route("/AgeProfiles" , methods=['GET', 'POST'])
def age_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(AgeProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = AgeProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(AgeProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgeProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgeProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  age_profiles_r(q_id):

    c = AgeProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(AgeProfiles), request.args):
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



@quantify_blueprint.route("/EntryExitProfiles" , methods=['GET', 'POST'])
def entry_exit_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(EntryExitProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = EntryExitProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(EntryExitProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = EntryExitProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/EntryExitProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  entry_exit_profiles_r(q_id):

    c = EntryExitProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(EntryExitProfiles), request.args):
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



@quantify_blueprint.route("/TourismIncomeSpendProfiles" , methods=['GET', 'POST'])
def tourism_income_spend_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(TourismIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = TourismIncomeSpendProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(TourismIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = TourismIncomeSpendProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/TourismIncomeSpendProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  tourism_income_spend_profiles_r(q_id):

    c = TourismIncomeSpendProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(TourismIncomeSpendProfiles), request.args):
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



@quantify_blueprint.route("/TourismProjectIncomeSpendProfiles" , methods=['GET', 'POST'])
def tourism_project_income_spend_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(TourismProjectIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = TourismProjectIncomeSpendProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(TourismProjectIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = TourismProjectIncomeSpendProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/TourismProjectIncomeSpendProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  tourism_project_income_spend_profiles_r(q_id):

    c = TourismProjectIncomeSpendProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(TourismProjectIncomeSpendProfiles), request.args):
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



@quantify_blueprint.route("/PassengerTransportProjectIncomeSpendProfiles" , methods=['GET', 'POST'])
def passenger_transport_project_income_spend_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(PassengerTransportProjectIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = PassengerTransportProjectIncomeSpendProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(PassengerTransportProjectIncomeSpendProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = PassengerTransportProjectIncomeSpendProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/PassengerTransportProjectIncomeSpendProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  passenger_transport_project_income_spend_profiles_r(q_id):

    c = PassengerTransportProjectIncomeSpendProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(PassengerTransportProjectIncomeSpendProfiles), request.args):
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



@quantify_blueprint.route("/ForeignDebtProfiles" , methods=['GET', 'POST'])
def foreign_debt_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ForeignDebtProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ForeignDebtProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ForeignDebtProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ForeignDebtProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ForeignDebtProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  foreign_debt_profiles_r(q_id):

    c = ForeignDebtProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ForeignDebtProfiles), request.args):
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



@quantify_blueprint.route("/EnvironmentalResourcesProfiles" , methods=['GET', 'POST'])
def environmental_resources_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(EnvironmentalResourcesProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = EnvironmentalResourcesProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(EnvironmentalResourcesProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = EnvironmentalResourcesProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/EnvironmentalResourcesProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  environmental_resources_profiles_r(q_id):

    c = EnvironmentalResourcesProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(EnvironmentalResourcesProfiles), request.args):
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



@quantify_blueprint.route("/PowerGenerationProfiles" , methods=['GET', 'POST'])
def power_generation_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(PowerGenerationProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = PowerGenerationProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(PowerGenerationProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = PowerGenerationProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/PowerGenerationProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  power_generation_profiles_r(q_id):

    c = PowerGenerationProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(PowerGenerationProfiles), request.args):
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



@quantify_blueprint.route("/EducationProfiles" , methods=['GET', 'POST'])
def education_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(EducationProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = EducationProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(EducationProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = EducationProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/EducationProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  education_profiles_r(q_id):

    c = EducationProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(EducationProfiles), request.args):
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



@quantify_blueprint.route("/FuelCostProfiles" , methods=['GET', 'POST'])
def fuel_cost_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(FuelCostProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = FuelCostProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(FuelCostProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = FuelCostProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/FuelCostProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  fuel_cost_profiles_r(q_id):

    c = FuelCostProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(FuelCostProfiles), request.args):
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



@quantify_blueprint.route("/TransportProfiles" , methods=['GET', 'POST'])
def transport_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(TransportProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = TransportProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(TransportProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = TransportProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/TransportProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  transport_profiles_r(q_id):

    c = TransportProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(TransportProfiles), request.args):
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



@quantify_blueprint.route("/InvestmentProfiles" , methods=['GET', 'POST'])
def investment_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(InvestmentProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = InvestmentProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(InvestmentProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = InvestmentProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/InvestmentProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  investment_profiles_r(q_id):

    c = InvestmentProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(InvestmentProfiles), request.args):
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



@quantify_blueprint.route("/AssistanceProfiles" , methods=['GET', 'POST'])
def assistance_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(AssistanceProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = AssistanceProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(AssistanceProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AssistanceProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AssistanceProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  assistance_profiles_r(q_id):

    c = AssistanceProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(AssistanceProfiles), request.args):
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



@quantify_blueprint.route("/MineralProfiles" , methods=['GET', 'POST'])
def mineral_profiles():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(MineralProfiles), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = MineralProfiles.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(MineralProfiles), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = MineralProfiles()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/MineralProfiles/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  mineral_profiles_r(q_id):

    c = MineralProfiles.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(MineralProfiles), request.args):
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



@quantify_blueprint.route("/AgricultureInvestmentCountry" , methods=['GET', 'POST'])
def agriculture_investment_country():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(AgricultureInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = AgricultureInvestmentCountry.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(AgricultureInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgricultureInvestmentCountry()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgricultureInvestmentCountry/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  agriculture_investment_country_r(q_id):

    c = AgricultureInvestmentCountry.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(AgricultureInvestmentCountry), request.args):
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



@quantify_blueprint.route("/ForeignInvestmentAgricultureForestryFisheriesPlace" , methods=['GET', 'POST'])
def foreign_investment_agriculture_forestry_fisheries_place():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheriesPlace), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ForeignInvestmentAgricultureForestryFisheriesPlace.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheriesPlace), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ForeignInvestmentAgricultureForestryFisheriesPlace()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ForeignInvestmentAgricultureForestryFisheriesPlace/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  foreign_investment_agriculture_forestry_fisheries_place_r(q_id):

    c = ForeignInvestmentAgricultureForestryFisheriesPlace.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheriesPlace), request.args):
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



@quantify_blueprint.route("/ForeignInvestmentAgricultureForestryFisheries" , methods=['GET', 'POST'])
def foreign_investment_agriculture_forestry_fisheries():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheries), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ForeignInvestmentAgricultureForestryFisheries.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheries), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ForeignInvestmentAgricultureForestryFisheries()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ForeignInvestmentAgricultureForestryFisheries/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  foreign_investment_agriculture_forestry_fisheries_r(q_id):

    c = ForeignInvestmentAgricultureForestryFisheries.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ForeignInvestmentAgricultureForestryFisheries), request.args):
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



@quantify_blueprint.route("/FDIInvestmentCountry" , methods=['GET', 'POST'])
def fdi_investment_country():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(FDIInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = FDIInvestmentCountry.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(FDIInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = FDIInvestmentCountry()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/FDIInvestmentCountry/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  fdi_investment_country_r(q_id):

    c = FDIInvestmentCountry.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(FDIInvestmentCountry), request.args):
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



@quantify_blueprint.route("/AgriculturalForeignInvestmentCountry" , methods=['GET', 'POST'])
def agricultural_foreign_investment_country():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(AgriculturalForeignInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = AgriculturalForeignInvestmentCountry.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(AgriculturalForeignInvestmentCountry), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = AgriculturalForeignInvestmentCountry()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/AgriculturalForeignInvestmentCountry/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  agricultural_foreign_investment_country_r(q_id):

    c = AgriculturalForeignInvestmentCountry.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(AgriculturalForeignInvestmentCountry), request.args):
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



@quantify_blueprint.route("/ForeignDirectInvestment" , methods=['GET', 'POST'])
def foreign_direct_investment():
    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        if not check_args(dir(ForeignDirectInvestment), request.args):
            return jsonify(status="fail", reason="error args", data=[])

        page = request.args.get('page')
        if page is None:
            page = 1

        query = ForeignDirectInvestment.query

        for k,v in request.args.items():
            query = query.filter_by(**{k: v})

        pagenation = query.paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'],
                                                    error_out=False)
        return jsonify(status="success", reason="", data=[item.to_json() for item in pagenation.items],
                       page={'current':pagenation.pages,'per_page':pagenation.per_page,'total':pagenation.total})

    if request.method == "POST":

        permission_required(Permission.QUANTIFY_W)

        form = request.form
        if not check_args(dir(ForeignDirectInvestment), request.args):
            return jsonify(status="fail", reason="error form args", data=[])

        c = ForeignDirectInvestment()

        for k, v in form.items():
            if hasattr(c, k):
                setattr(c, k, v)

        db.session.add(c)
        db.session.commit()

        return jsonify(status="success", reason="", data=[c.to_json()])


@quantify_blueprint.route("/ForeignDirectInvestment/<q_id>", methods=['GET', 'PUT', 'DELETE'])
def  foreign_direct_investment_r(q_id):

    c = ForeignDirectInvestment.query.filter_by(id=q_id).first()

    if c is None:
        return jsonify(status="fail", reason="no this id thing", data=[])

    if request.method == "GET":

        permission_required(Permission.QUANTIFY_R)

        return jsonify(status="success", reason="", data=[c.to_json()])

    if request.method == "PUT":
        form = request.form

        permission_required(Permission.QUANTIFY_W)

        if not check_args(dir(ForeignDirectInvestment), request.args):
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


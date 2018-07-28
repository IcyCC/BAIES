#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/27 2:00 PM
# @Author  : suchang
# @File    : setup_proj.py

from flask import current_app
from app import db, create_app
from app.model.user import User,Role
from app.model.quantify import Country
from app.model.qualitative.information import Kind

if __name__ == '__main__':
    app = create_app('development')
    app_ctx = app.app_context()
    app_ctx.push()

    print("建立数据表")
    db.create_all()

    print("新增国家")
    cn = Country(name="China", en_alis="china", cn_alis="中国")
    db.session.add(cn)
    br = Country(name="Brazil", en_alis="brazil", cn_alis="巴西")
    db.session.add(br)
    ind = Country(name="India", en_alis="india", cn_alis="印度")
    db.session.add(ind)
    ru = Country(name="Russia", en_alis="russia", cn_alis="俄罗斯")
    db.session.add(ru)
    sa = Country(name="SouthAfrica", en_alis="south africa", cn_alis="南非")
    db.session.add(sa)
    db.session.commit()

    print("新增类别")
    adp = Kind(id=1, name="adp", en_alis="Agricultural Development Policies", cn_alis="农业发展政策")
    db.session.add(adp)
    atp = Kind(id=2, name="atp", en_alis="Agricultural Trade Policies", cn_alis="农业贸易政策")
    db.session.add(atp)
    ast = Kind(id=3, name="ast", en_alis="Agricultural Science and Technology", cn_alis="农业科学与技术")
    db.session.add(ast)
    fap = Kind(id=4, name="fap", en_alis="Fishery & Aquaculture Policies", cn_alis="渔业水产政策")
    db.session.add(fap)
    db.session.commit()

    print("插入角色")
    Role.insert_roles()

    print("建立管理员")

    u = User(email="admin@admin.com", username="admin", role_id=Role.query.filter_by(name='Administrator').first().id,
             country_id=Country.query.filter_by(name="China").first().id)

    u.password = "admin1010"

    db.session.add(u)
    db.session.commit()

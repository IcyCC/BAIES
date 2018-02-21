from app.model.qualitative.information import *
from app import db
from app.model.quantify.socioeconomic import *
from app.model.comm.log import *
from app.model.user import *

from sqlalchemy.exc import IntegrityError
from faker import Faker
from random import randint
import requests


def insert_country():
    c1 = Country(name='CN',cn_alis="中国", en_alis="China")
    db.session.add(c1)

    c2 = Country(name='EN', cn_alis="英国", en_alis="England")
    db.session.add(c2)

    c3 = Country(name='US', cn_alis="美国", en_alis="USA")
    db.session.add(c3)

    db.session.commit()

def insert_kind():
    k1 = Kind(name= '农业发展政策信息',
              cn_alis='农业发展政策信息',
              en_alis='Agricultural Development')
    db.session.add(k1)

    k2 = Kind(name= '农业贸易政策信息',
              cn_alis='农业贸易政策信息',
              en_alis='Agricultural Trade')
    db.session.add(k2)

    k3 = Kind(name='农业科技政策信息',
              cn_alis='农业科技政策信息',
              en_alis='Agricultural Science and Technology')
    db.session.add(k3)

    k4 = Kind(name='鱼林政策信息',
              cn_alis='鱼林政策信息',
              en_alis='Fishery & Aquaculture Policies')
    db.session.add(k4)

    db.session.commit()

def insert_post(count=100):
    fake = Faker(locale='zh_CN')
    i=0

    k_count = Kind.query.count()
    if k_count == 0:
        insert_kind()
    k_count = Kind.query.count()
    print("COUNT K", k_count)
    while i<count:
        k = Kind.query.offset(randint(0, k_count-1)).first()
        d = Post(
            title=fake.sentence(),
            body=fake.text(),
            kind_id=k.id,
            user_id=-1,
            show=False
        )
        db.session.add(d)
        print("ADD", d)

        try:
            db.session.commit()
            i += 1
        except IntegrityError:
            print("EXCEPETION")
            db.session.rollback()



def insert_test_soc_data():
    load = {
        "name": 'A',
        "cn_alis": 'ATable',
        "en_alis": 'A表',
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_table",data=load)

    load = {
        "name": 'B',
        "cn_alis": 'BTable',
        "en_alis": 'B表',
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_table",data=load)

    load = {
        "name": 'C',
        "cn_alis": 'CTable',
        "en_alis": 'C表',
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_table", data=load)

    load = {
        "name": 'a',
        "cn_alis": 'aindex',
        "en_alis": 'a指标',
        "table_id": 1
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_index", data=load)

    load = {
        "name": 'b',
        "cn_alis": 'bindex',
        "en_alis": 'b指标',
        "table_id": 1
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_index", data=load)

    load = {
        "name": 'c',
        "cn_alis": 'cindex',
        "en_alis": 'c指标',
        "table_id": 1
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_index", data=load)

    load = {
        "name": 'd',
        "cn_alis": 'dindex',
        "en_alis": 'd指标',
        "table_id": 2
    }
    requests.post("http://127.0.0.1:5000/quantify/socioeconomic_index", data=load)


def gen():
    Role.insert_roles()
    insert_country()
    insert_post()
    insert_test_soc_data()
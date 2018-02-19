from app.model.qualitative.information import Post, Kind
from app import db
from sqlalchemy.exc import IntegrityError
from faker import Faker
from random import randint
import requests

def insert_post(count=100):
    fake = Faker(locale='zh_CN')
    i=0
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


def insert_test_data():
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


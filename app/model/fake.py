from app.model.qualitative.information import Post, Kind
from app import db
from sqlalchemy.exc import IntegrityError
from faker import Faker
from random import randint

def datas(count=100):
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
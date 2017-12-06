from app import db,login_manager
from flask_login import UserMixin, AnonymousUserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort,jsonify
from functools import wraps

class Permission:

    # PERMISSION 0b0000000000
    # 权限依次

    QUANTIFY_R = 0x01
    QUANTIFY_W = 0x02

    QUALITATIVE_R = 0x04
    QUALITATIVE_W = 0x08

    USER = 0x10
    SYSTEM = 0x20



class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    country = db.Column(db.String(64))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, perm):
        return self.role is not None and self.role.has_permission(perm)

    def to_json(self):
        return {
            'id':self.id,
            'email': self.email,
            'username': self.username,
            'role_id': self.role_id,
            'country': self.country
        }


class AnonymousUser(AnonymousUserMixin):

    permissions = Permission.QUALITATIVE_R

    def can(self, permissions):
        return permissions & self.permissions  == permissions


login_manager.anonymous_user = AnonymousUser


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,index=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    def to_json(self):
        return {
            'id':self.id,
            'name': self.name,
            'permissions': self.permissions,
        }

    roles = {
        'User': (Permission.QUANTIFY_R,
                 Permission.QUALITATIVE_R, True),
        'CountryQualitative': (Permission.QUANTIFY_R | Permission.QUALITATIVE_R
                               | Permission.QUALITATIVE_W, False),
        'CountryQuantify': (Permission.QUANTIFY_R | Permission.QUANTIFY_W | Permission.QUALITATIVE_R, False),
        'Administrator': (0xff, False)
    }

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.QUANTIFY_R,
                     Permission.QUALITATIVE_R, True),
            'CountryQualitative': (Permission.QUANTIFY_R|Permission.QUALITATIVE_R
                                    | Permission.QUALITATIVE_W, False),
            'CountryQuantify': (Permission.QUANTIFY_R|Permission.QUANTIFY_W|Permission.QUALITATIVE_R, False),
            'Administrator': (0xff, False)
        }
        for r in roles.keys():
            role = Role.query.filter_by(name=r).first()
            if role is None:
                print(r)
                role = Role(name=r)
            role.permissions = roles[r][0]
            db.session.add(role)
        db.session.commit()

    def has_permission(self, perm):
        return self.permissions & perm == perm


def permission_required_d(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                return jsonify(status="fail", data=[], reason="no permission")
            return f(*args, **kwargs)
        return decorated_function
    return decorator



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
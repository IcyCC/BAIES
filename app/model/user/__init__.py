from app import db,login_manager
from flask_login import UserMixin, AnonymousUserMixin,current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask import abort,jsonify
from functools import wraps

class Permission:

    # PERMISSION 0b0000000000
    # 权限依次

    QUANTIFY_R = 0x01 # 定量信息读
    QUANTIFY_W = 0x02 # 定量信息写

    QUALITATIVE_R = 0x04 # 定性信息读
    QUALITATIVE_W = 0x08 # 定性信息写

    USER_R = 0x10 # 用户信息读
    USER_W = 0x20 # 用户信息写

    SYSTEM_R = 0x40 # 系统信息读
    SYSTEM_W = 0X80 # 系统信息写





class User(db.Model, UserMixin):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), index=True)
    country = db.Column(db.String(64))

    @property
    def role(self):
        t = Role.query.filter(Role.id == self.role_id).first()
        return t

    @property
    def posts(self):
        from app.model.qualitative.information import Post
        t = Post.query.join(User, User.id == Post.user_id).filter(self.id == Post.kind_id).all()
        return t

    @property
    def logs(self):
        from app.model.comm.log import Log
        t = Log.query.join(User, User.id == Log.user_id).filter(self.id == Log.user_id).all()
        return t

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
            'country': self.country,
            'role': self.role.to_json()
        }


class AnonymousUser(AnonymousUserMixin):

    id = -1
    permissions = Permission.QUALITATIVE_R

    def can(self, permissions):
        return permissions & self.permissions  == permissions

    def to_json(self):
        return {
            "id": -1,
            "username": "Anonymous",
            "role": "Anonymous",
            "country":"NU"
        }


login_manager.anonymous_user = AnonymousUser


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True ,index=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer)


    @property
    def users(self):
        t = User.query.join(Role, Role.id == User.role_id).filter(User.id == self.user_id).all()
        return t

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
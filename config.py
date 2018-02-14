import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_COMMIT_TEARDOWN = True
    UPLOAD_FOLDER = basedir+'/app/static/upload'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        "mysql://root:root@127.0.0.1:3306/baies?charset=utf8mb4"
    FLASKY_POSTS_PER_PAGE = 2000
    CONFIG_NAME = "dev"
    SQLALCHEMY_ECHO = True
    SECRET_KEY = 'hard to guess string'



class RunConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = \
        'mysql://root:root@'+'localhost/'+'baies'
    CONFIG_NAME = "run"
    SECRET_KEY = 'hard to guess string'
    FLASKY_POSTS_PER_PAGE = 2000

config = {
    'development': DevelopmentConfig,
    'run': RunConfig
}
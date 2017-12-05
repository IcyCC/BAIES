from flask import Blueprint

user_blueprint = Blueprint("user", __name__)

from .action import *
from .user import *

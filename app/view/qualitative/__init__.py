from flask import Blueprint

qualitative_blueprint = Blueprint("qualitative", __name__)

from .information import *

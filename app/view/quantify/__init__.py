from flask import Blueprint

quantify_blueprint = Blueprint("quantify", __name__)

#from .socioeconomic import *
from .socioeconomic_a import *
from .agriculture_products_a import *

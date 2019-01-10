from flask import Blueprint

bp = Blueprint('portfolio', __name__)

from forcewing.portfolio import routes
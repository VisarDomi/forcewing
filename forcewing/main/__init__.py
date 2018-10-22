from flask import Blueprint

bp = Blueprint('main', __name__)

from forcewing.main import routes
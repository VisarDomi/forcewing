from flask import Blueprint 

bp = Blueprint('errors', __name__)

from forcewing.errors import routes
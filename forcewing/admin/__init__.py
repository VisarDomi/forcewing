from flask import Blueprint

bp = Blueprint('admin', __name__)

from forcewing.admin import routes
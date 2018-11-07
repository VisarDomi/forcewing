from flask import Blueprint

bp = Blueprint('blog', __name__)

from forcewing.blog import routes
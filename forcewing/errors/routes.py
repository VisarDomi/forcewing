from flask import render_template
from forcewing.main.forms import LoginForm
from forcewing.errors import bp

@bp.errorhandler(404)
def error_404(error):
    loginForm = LoginForm()
    return render_template('errors/404.html', loginForm=loginForm), 404


@bp.errorhandler(403)
def error_403(error):
    loginForm = LoginForm()

    return render_template('errors/403.html', loginForm=loginForm), 403

@bp.errorhandler(401)
def error_401(error):
    loginForm = LoginForm()

    return render_template('errors/401.html', loginForm=loginForm), 401


@bp.errorhandler(500)
def error_500(error):
    loginForm = LoginForm()

    return render_template('errors/500.html', loginForm=loginForm), 500



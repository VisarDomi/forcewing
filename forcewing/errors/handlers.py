from flask import render_template, redirect, flash, url_for
from flask_login import login_user
from forcewing import app, bcrypt
from forcewing.models import User
from forcewing.forms import LoginForm


@app.errorhandler(404)
def error_404(error):
    loginForm = LoginForm()
    return render_template('errors/404.html', loginForm=loginForm), 404


@app.errorhandler(403)
def error_403(error):
    loginForm = LoginForm()

    return render_template('errors/403.html', loginForm=loginForm), 403

@app.errorhandler(401)
def error_401(error):
    loginForm = LoginForm()

    return render_template('errors/401.html', loginForm=loginForm), 401


@app.errorhandler(500)
def error_500(error):
    loginForm = LoginForm()

    return render_template('errors/500.html', loginForm=loginForm), 500
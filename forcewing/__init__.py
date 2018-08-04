from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt 
from flask_mail import Mail 

app = Flask(__name__)
app.config['SECRET_KEY'] = '3028jr082j2r30930fj2kdjvaldvmoween'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False 
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'forcewing.worker@gmail.com'#!!!!!
app.config['MAIL_PASSWORD'] = 'ImpresaWorker123'
mail = Mail(app)

db = SQLAlchemy(app)
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)

from forcewing.errors import handlers
from forcewing import routes
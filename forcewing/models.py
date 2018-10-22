from datetime import datetime
from flask_login import UserMixin
from forcewing import db, login_manager

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    image_file = db.Column(db.String(20), nullable=False, default='Dead_Dragon.png')
    #email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Blog', backref='author', lazy=True)

    def __repr__(self):
        return f"User(('{self.username}'), {self.image_file}"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable=False, unique=True)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #here
    image_file = db.Column(db.String(20), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(1000), nullable=False)
    subtitle = db.Column(db.String(1000), default='Placeholder')
    section_title = db.Column(db.String(3000), default='Placeholder')
    content = db.Column(db.Text, nullable=False)
    subsection_title = db.Column(db.String(3000), default='Placeholder')
    quote = db.Column(db.String(200), default='Placeholder')
    #First\r\nSecond line\r\n\r\n
    category = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Blog(('{self.title}'), ('{self.user_id}')"

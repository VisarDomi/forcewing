from datetime import datetime
from flask_login import UserMixin
from forcewing import db, login_manager

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    image_file = db.Column(db.String(100), nullable=False, default='Dead_Dragon.png')
    #email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    posts = db.relationship('Blog', backref='author', lazy=True)
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)

    def __repr__(self):
        return f"User(('{self.username}', {self.image_file}"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Category(db.Model):
    """no relationships with other classes"""
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    def __repr__(self):
        return f"Category('{self.name}')"

class Blog(db.Model):
    """
    One to many relationship with User
    one -> User
    many-> Blog
    user.posts
    blog.author
    """
    __tablename__ = 'blogs'
    id = db.Column(db.Integer, primary_key=True)
    #here
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(1000), nullable=False)
    subtitle = db.Column(db.String(1000), default='Subtitle')
    content = db.Column(db.Text, nullable=False)
    section_title = db.Column(db.String(3000), default='Section title')
    subsection_title = db.Column(db.String(3000), default='Subsection title')
    quote = db.Column(db.String(200), default='Quote')
    #First\r\nSecond line\r\n\r\n
    category = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Blog('{self.title}', '{self.user_id}')"

class Tag(db.Model):
    """no relationships with other classes"""
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

    def __repr__(self):
        return f"Tag('{self.name}')"

class Portfolio(db.Model):
    """
    One to many relationship with User
    one -> User
    many-> Portfolio
    user.portfolios
    portfolio.user
    """
    __tablename__ = 'portfolios'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), nullable=False)
    subtitle = db.Column(db.String(1000), default='Subtitle')
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    tag = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100), nullable=False)
    client_logo = db.Column(db.String(100), nullable=False)
    client_name = db.Column(db.String(100), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Portfolio('{self.title}')"

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from forcewing import db, login_manager



class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    image_file = db.Column(db.String(100), default='Dead_Dragon.png')
    #email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    
    posts = db.relationship('Blog', backref='author', lazy=True)
    portfolios = db.relationship('Portfolio', backref='user', lazy=True)

    def __repr__(self):
        return f"User(('{self.username}', {self.image_file}"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class Category(db.Model):
    """
    No relationships with other classes.

    Needs to have many to many relationship with Blog.
    """
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
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.String(1000), nullable=False)
    subtitle = db.Column(db.String(1000))
    section_title = db.Column(db.String(3000))
    section_content = db.Column(db.Text, nullable=False)
    subsection_title = db.Column(db.String(3000))
    subsection_content = db.Column(db.Text)
    quote = db.Column(db.String(1000))
    #First\r\nSecond line\r\n\r\n
    category = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(100))

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
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    title = db.Column(db.String(1000), nullable=False)
    subtitle = db.Column(db.String(1000), default='Subtitle')
    content = db.Column(db.Text, nullable=False)
    tag = db.Column(db.String(100), nullable=False)
    image_file1 = db.Column(db.String(100))
    image_file2 = db.Column(db.String(100))
    image_file3 = db.Column(db.String(100))
    client_logo = db.Column(db.String(100))
    client_name = db.Column(db.String(100))

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Portfolio('{self.title}')"

from flask import render_template, redirect, url_for, flash
from flask_mail import Message
from flask_login import current_user, login_user, logout_user
from forcewing import mail
from forcewing.main import bp
from forcewing.main.forms import LoginForm, ContactForm
from forcewing.models import User, Blog, Category, Portfolio, Tag

#main
def send_contact_email(name, email, message):
    #send a email to recipients from sender with the following arguments as information

    msg = Message('Forcewing', sender='forcewing.worker@gmail.com', recipients=['ronalddomi4@gmail.com'])
    msg.body = f'''Someone just submitted your form on forcewing.com, here's what they had to say:
    ------
    Name:  {name}

    Email:  {email}

    Message:  {message}
    
    '''
    mail.send(msg)

# main

@bp.route('/', methods=['GET', 'POST'])
@bp.route('/home', methods=['GET', 'POST'])
def index():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    portfolios = Portfolio.query.order_by(Portfolio.date_posted.desc()).limit(6).all()
    contactForm = ContactForm()
    loginForm = LoginForm()
    categories = Category.query.all()
    tags = Tag.query.all()

    return render_template('index.html', 
                            blogs=blogs, 
                            portfolios=portfolios, 
                            loginForm=loginForm, 
                            contactForm=contactForm, 
                            categories=categories,
                            tags=tags)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user is None or not user.check_password(loginForm.password.data):
            flash('Invalid username or password')
            return redirect(url_for('admin.admin_page'))
        login_user(user, remember=loginForm.remember.data)
        return redirect(url_for('admin.admin_page'))
    return render_template('login.html', title='Sign In', loginForm=loginForm)

@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@bp.route('/contact', methods=['POST', 'GET'])
def contactForm():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    loginForm = LoginForm()
    contactForm = ContactForm()

    print('ready to get validated')
    if contactForm.validate_on_submit():
        print('validated')
        send_contact_email(contactForm.name.data, 
                           contactForm.email.data,
                        #    contactForm.subject.data,
                           contactForm.message.data)
        return redirect(url_for('main.form_sent'))

    return render_template('index.html', blogs=blogs, loginForm=loginForm, contactForm=contactForm)

@bp.route('/form_sent', methods=['GET', 'POST'])
def form_sent():
    return render_template('contact.html')

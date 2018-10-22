from flask import render_template, redirect, url_for
from flask_mail import Message
from flask_login import login_user, logout_user
from forcewing import bcrypt, mail
from forcewing.main import bp
from forcewing.main.forms import LoginForm, ContactForm
from forcewing.models import User, Blog

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
    contactForm = ContactForm()
    loginForm = LoginForm()

    return render_template('index.html', blogs=blogs, loginForm=loginForm, contactForm=contactForm)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    #blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    loginForm = LoginForm()
    #contactForm = ContactForm()

    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        # hashed_password = bcrypt.generate_password_hash(loginForm.password.data).decode('utf-8')
        if loginForm.username.data == 'Forcewing' and bcrypt.check_password_hash(user.password, loginForm.password.data):
            login_user(user, remember=loginForm.remember.data)
            return redirect(url_for('main.admin_page'))

    return render_template('login.html', loginForm=loginForm)

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

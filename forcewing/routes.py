import secrets, os
from PIL import Image, ImageOps
from flask import render_template, redirect, url_for, flash, request, abort
from forcewing import app, db, bcrypt, mail
from flask_mail import Message
from forcewing.forms import LoginForm, BlogForm, UpdateAccountInformationForm
from forcewing.forms import UpdateAccountPhotoForm, UpdateBlogForm, CategoryForm, ContactForm
from forcewing.models import User, Blog, Category
from flask_login import login_user, current_user, logout_user, login_required

#--------------------------------
def change_text(id):
    blog = Blog.query.filter_by(id=id).first()
    lines = blog.content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string=str(text)
            html.append(string)
    return html
#--------------------------------
def send_contact_email(name, phone, subject, message):
    #send a email to recipients from sender with the following arguments as information

    msg = Message(subject, sender='impresa.worker@gmail.com', recipients=['erdal.domi@gmail.com'])
    msg.body = f'''Someone just submitted your form on impresaprivacy.com, here's what they had to say:
    ------
    Name:  {name}

    Phone:  {phone}

    Subject:  {subject}

    Message:  {message}
    
    '''
    mail.send(msg)

def save_picture(form_picture, dest_folder, output_size_1, output_size_2):
    #save_picture saves picture from user input to static folder, hashing the filename  
    #form_picture is the file name of the input
    #desc_folder is the folder where the image is 
    random_hex = secrets.token_hex(8) #8 bytes 
    _, f_ext = os.path.splitext(form_picture.filename)

    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/', dest_folder, picture_fn)

    output_size = (output_size_1, output_size_2)
    i = Image.open(form_picture)
    i = i.convert('RGB')
    # i.thumbnail(output_size)
    i = ImageOps.fit(i, output_size, Image.ANTIALIAS)

    i.save(picture_path)

    return picture_fn



@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def index():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    contactForm = ContactForm()
    loginForm = LoginForm()

    return render_template('index.html', blogs=blogs, loginForm = loginForm, contactForm=contactForm)

@app.route('/login', methods=['POST'])
def login():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    loginForm = LoginForm()
    contactForm = ContactForm()

    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        hashed_password = bcrypt.generate_password_hash(loginForm.password.data).decode('utf-8')
        if loginForm.username.data == 'Matteo' and bcrypt.check_password_hash(user.password, loginForm.password.data):
            login_user(user, remember=True)
            return redirect(url_for('admin_page'))

    return render_template('index.html', blogs=blogs, loginForm = loginForm, contactForm=contactForm)

@app.route('/contact', methods=['POST'])
def contactForm():
    blogs = Blog.query.order_by(Blog.date_posted.desc()).limit(3).all()
    loginForm = LoginForm()
    contactForm = ContactForm()

    if contactForm.validate_on_submit():
        send_contact_email(contactForm.name.data, 
                           contactForm.phone.data,
                           contactForm.subject.data,
                           contactForm.message.data)
        return redirect(url_for('form_sent'))

    return render_template('index.html', blogs=blogs, loginForm = loginForm, contactForm=contactForm)

@app.route('/bloglist', methods=['GET', 'POST'])
def bloglist():
    blogs = Blog.query.paginate(per_page=5)

    loginForm = LoginForm()
   
    return render_template('bloglist.html',loginForm=loginForm ,title='Blog posts', blogs=blogs)

@app.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    returnedHtml = change_text(blog_id)
    loginForm = LoginForm()

    
    return render_template('blog.html', title=blog.title, blog=blog, loginForm=loginForm, returnedHtml=returnedHtml)

@app.route('/blog/<string:category>')
def filtered_blogs(category):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    blogs = Blog.query.filter_by(category=category)\
            .order_by(Blog.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('blog-category.html',form=form, title=category, category=category, blogs=blogs)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/form_sent')
def form_sent():
    return render_template('contact.html')





@app.route('/admin/admin-page', methods=['POST', 'GET'])
@login_required
def admin_page():
    # form = LoginForm()
    user = User.query.first()
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-page.html', title='Admin Page', image_file = image_file, user=user, blogs=blogs)

@app.route('/admin/profile/information', methods=['POST', 'GET'])
@login_required
def admin_update_information():
    form = UpdateAccountInformationForm()
    user = User.query.first()
    if form.validate_on_submit():
        user.username = form.username.data 
        db.session.commit()
        return redirect(url_for('admin_update_information'))
    elif request.method == 'GET':
        form.username.data = user.username 
    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-information.html', title='Update Account', image_file=user_image_file, form=form, user=user)

@app.route('/admin/profile/photo', methods=['POST', 'GET'])
@login_required
def admin_update_photo():
    form = UpdateAccountPhotoForm()
    user = User.query.first()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'profile_pics', 130, 130)
            user.image_file = picture_file
        # user.username = form.username.data 
        db.session.commit()
        return redirect(url_for('admin_update_photo'))
    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-photo.html', title='Update Account', image_file=user_image_file, form=form, user=user)





@app.route('/admin/blog/new', methods=['POST', 'GET'])
@login_required
def blog_new():
    
    form = BlogForm() 
    
    choiceList = [(choice.name, choice.name) for choice in Category.query.all()]
    form.category.choices = choiceList
    
    user = User.query.first()
   
    if form.validate_on_submit():

        image_file = save_picture(form.image_file.data, 'blog_pics', 900, 900)
        photo_image_file = url_for('static', filename='blog_pics/' + image_file)
    
        user = User.query.first()
        blog = Blog(title= form.title.data, content=form.content.data, quote = form.quote.data, 
        image_file=photo_image_file, section_title=form.section_title.data, author=user, subsection_title=form.subsection_title.data, 
        subtitle=form.subtitle.data, category=form.category.data)
    
        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('admin_page'))

    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-new.html', title='New Blog', form=form, user=user, image_file = image_file)

@app.route('/admin/blog/<int:blog_id>/delete', methods=['GET', 'POST'])
@login_required
def blog_delete(blog_id):
	blog = Blog.query.get_or_404(blog_id)
	# if blog.author != current_user:
	# 	abort(403)
	db.session.delete(blog)
	db.session.commit()
	return redirect(url_for('admin_page'))

@app.route('/admin/blog/<int:blog_id>/update', methods=['POST', 'GET'])
@login_required
def blog_update(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    user = User.query.first()
    form = UpdateBlogForm()

    choiceList = [(choice.name, choice.name) for choice in Category.query.all()]
    form.category.choices = choiceList
    print(form.validate_on_submit())
    if form.validate_on_submit():
        blog.title = form.title.data 
        blog.subtitle = form.subtitle.data
        blog.section_title = form.section_title.data 
        blog.content = form.content.data 
        blog.quote = form.quote.data 
        blog.subsection_title = form.subsection_title.data 
        blog.category = form.category.data
        #image_file is the input name
        if 'image_file' in request.files:
            image_file = save_picture(form.image_file.data, 'blog_pics', 900, 900)
            photo_image_file = url_for('static', filename='blog_pics/' + image_file)
            blog.image_file = photo_image_file

        db.session.commit()
        return redirect(url_for('admin_page'))
        
    elif request.method == 'GET':
        form.title.data = blog.title  
        form.subtitle.data = blog.subtitle
        form.section_title.data = blog.section_title
        form.content.data = blog.content 
        form.subsection_title.data = blog.subsection_title 
        form.quote.data = blog.quote
        form.category.data = blog.category
        # if blog.image_file:
            # form.image_file = blog.image_file

    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-update.html', title='Update Blog', user=user, image_file=user_image_file,
                form=form, legend='Update Blog')

@app.route('/admin/category/<int:category_id>/delete', methods=['GET', 'POST'])
@login_required
def category_delete(category_id):
	category = Category.query.get_or_404(category_id)
	db.session.delete(category)
	db.session.commit()
	return redirect(url_for('category'))

@app.route('/admin/category', methods=['GET', 'POST'])
def category():
    user = User.query.first()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    form = CategoryForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        tag = Category(name=form.category_type.data)
        db.session.add(tag)
        db.session.commit()
        
        
        return redirect(url_for('category'))

    return render_template('admin/category.html', title='Category', image_file=image_file, user=user, form=form, categories=categories) 


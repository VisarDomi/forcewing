import secrets, os, shutil
from PIL import Image, ImageOps
from flask import render_template, redirect, url_for, request
from flask_login import login_required
from forcewing import db
from forcewing.admin import bp
from forcewing.main.forms import LoginForm
from forcewing.admin.forms import CategoryForm, BlogForm, UpdateBlogForm
from forcewing.admin.forms import UpdateAccountInformationForm, UpdateAccountPhotoForm
from forcewing.admin.forms import TagForm, PortfolioForm, UpdatePortfolioForm
from forcewing.models import User, Blog, Category, Portfolio, Tag

#admin
def save_picture(form_picture, dest_folder, output_size_1, output_size_2):
    """
    save_picture saves picture from user input to static folder, hashing the filename  
    form_picture is the file name of the input
    dest_folder is the folder where the image is
    """
    random_hex = secrets.token_hex(8) #8 bytes
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(os.path.dirname(bp.root_path), 'static/', dest_folder, picture_fn)
    output_size = (output_size_1, output_size_2)
    i = Image.open(form_picture)
    i = i.convert('RGB')
    i = ImageOps.fit(i, output_size, Image.ANTIALIAS)
    i.save(picture_path)
    return picture_fn

# admin

@bp.route('/admin/admin-page', methods=['POST', 'GET'])
@login_required
def admin_page():
    # form = LoginForm()
    user = User.query.first()
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-page.html', title='Admin Page', image_file=image_file, user=user, blogs=blogs)

@bp.route('/admin/portfolio-page', methods=['POST', 'GET'])
@login_required
def portfolio_page():
    # form = LoginForm()
    user = User.query.first()
    portfolio = Portfolio.query.order_by(Portfolio.date_posted.desc()).all()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/portfolio-page.html', title='Portfolio Page', image_file=image_file, user=user, portfolios=portfolio)

# profile
@bp.route('/admin/profile/information', methods=['POST', 'GET'])
@login_required
def admin_update_information():
    form = UpdateAccountInformationForm()
    user = User.query.first()
    if form.validate_on_submit():
        user.username = form.username.data
        db.session.commit()
        return redirect(url_for('admin.admin_update_information'))
    elif request.method == 'GET':
        form.username.data = user.username
    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-information.html', title='Update Account', image_file=user_image_file, form=form, user=user)

@bp.route('/admin/profile/photo', methods=['POST', 'GET'])
@login_required
def admin_update_photo():
    form = UpdateAccountPhotoForm()
    user = User.query.first()
    if form.validate_on_submit():

        directory = os.path.join(os.path.dirname(bp.root_path), 'static/profile_pics/')
        recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin')
        directory_recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin/profile_pics')

        if os.path.exists(directory):
            if os.path.exists(directory_recycle_bin):
                shutil.rmtree(directory_recycle_bin)
            shutil.move(directory, recycle_bin)
            os.makedirs(directory)
        else:
            os.makedirs(directory)
        
        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'profile_pics', 130, 130)
            user.image_file = picture_file
        db.session.commit()
        return redirect(url_for('admin.admin_update_photo'))
    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-photo.html', title='Update Account', image_file=user_image_file, form=form, user=user)

# blog
@bp.route('/admin/blog/new', methods=['POST', 'GET'])
@login_required
def blog_new():

    form = BlogForm() 

    choiceList = [(choice.name, choice.name) for choice in Category.query.all()]
    form.category.choices = choiceList

    user = User.query.first()

    if form.validate_on_submit():

        folder_name = form.title.data
        directory = os.path.join(os.path.dirname(bp.root_path), 'static/', 'blog_pics/', folder_name)
        recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin')
        directory_recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin/', folder_name)

        if os.path.exists(directory):
            if os.path.exists(directory_recycle_bin):
                shutil.rmtree(directory_recycle_bin)
            shutil.move(directory, recycle_bin)
            os.makedirs(directory)
        else:
            os.makedirs(directory)
        
        image_file = save_picture(form.image_file.data, 'blog_pics/' + folder_name, 900, 900)
        photo_image_file = url_for('static', filename='blog_pics/' + folder_name + '/' + image_file)

        user = User.query.first()
        blog = Blog(title=form.title.data, 
                    subtitle=form.subtitle.data, 
                    section_title=form.section_title.data, 
                    section_content=form.section_content.data, 
                    subsection_title=form.subsection_title.data,
                    subsection_content=form.subsection_content.data,
                    quote=form.quote.data, 
                    category=form.category.data,
                    image_file=photo_image_file, 
                    author=user) 

        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('admin.admin_page'))

    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-new.html', title='New Blog', form=form, user=user, image_file=image_file)

@bp.route('/admin/blog/<int:blog_id>/update', methods=['POST', 'GET'])
@login_required
def blog_update(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    user = User.query.first()
    form = UpdateBlogForm()

    choiceList = [(choice.name, choice.name) for choice in Category.query.all()]
    form.category.choices = choiceList

    if form.validate_on_submit():

        folder_name = form.title.data
        directory = os.path.join(os.path.dirname(bp.root_path), 'static/', 'blog_pics/', folder_name)
        recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin')
        directory_recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin/', folder_name)

        if os.path.exists(directory):
            if os.path.exists(directory_recycle_bin):
                shutil.rmtree(directory_recycle_bin)
            shutil.move(directory, recycle_bin)
            os.makedirs(directory)
        else:
            os.makedirs(directory)

        blog.title = form.title.data 
        blog.subtitle = form.subtitle.data
        blog.section_title = form.section_title.data 
        blog.section_content = form.section_content.data 
        blog.subsection_title = form.subsection_title.data 
        blog.subsection_content = form.subsection_content.data 
        blog.quote = form.quote.data 
        blog.category = form.category.data

        #image_file is the input name
        if 'image_file' in request.files:
            image_file = save_picture(form.image_file.data, 'blog_pics/' + folder_name, 900, 900)
            photo_image_file = url_for('static', filename='blog_pics/' + folder_name + '/' + image_file)
            blog.image_file = photo_image_file

        db.session.commit()
        return redirect(url_for('admin.admin_page'))

    elif request.method == 'GET':
        form.title.data = blog.title
        form.subtitle.data = blog.subtitle
        form.section_title.data = blog.section_title
        form.section_content.data = blog.section_content
        form.subsection_title.data = blog.subsection_title
        form.subsection_content.data = blog.subsection_content
        form.quote.data = blog.quote
        form.category.data = blog.category
        # if blog.image_file:
            # form.image_file = blog.image_file

    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-update.html', 
                            title='Update Blog', 
                            user=user, 
                            image_file=user_image_file,
                            form=form, 
                            legend='Update Blog')

@bp.route('/admin/blog/<int:blog_id>/delete', methods=['GET', 'POST'])
@login_required
def blog_delete(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('admin.admin_page'))

# category
@bp.route('/admin/category', methods=['GET', 'POST'])
def category():
    user = User.query.first()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    form = CategoryForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        category = Category(name=form.category_type.data)
        db.session.add(category)
        db.session.commit()


        return redirect(url_for('admin.category'))

    return render_template('admin/category.html', title='Category', image_file=image_file, user=user, form=form, categories=categories) 

@bp.route('/admin/category/<int:category_id>/delete', methods=['GET', 'POST'])
@login_required
def category_delete(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.category'))

# portfolio
@bp.route('/admin/portfolio/new', methods=['POST', 'GET'])
@login_required
def portfolio_new():

    form = PortfolioForm() 

    choiceList = [(choice.name, choice.name) for choice in Tag.query.all()]
    form.tag.choices = choiceList

    user = User.query.first()

    if form.validate_on_submit():

        folder_name = form.title.data
        directory = os.path.join(os.path.dirname(bp.root_path), 'static/', 'portfolio_pics/', folder_name)
        recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin')
        directory_recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin/', folder_name)

        if os.path.exists(directory):
            if os.path.exists(directory_recycle_bin):
                shutil.rmtree(directory_recycle_bin)
            shutil.move(directory, recycle_bin)
            os.makedirs(directory)
        else:
            os.makedirs(directory)
        
        
        image_file1 = save_picture(form.image_file1.data, 'portfolio_pics/' + folder_name, 900, 900)
        photo_image_file1 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file1)
        image_file2 = save_picture(form.image_file2.data, 'portfolio_pics/' + folder_name, 900, 900)
        photo_image_file2 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file2)
        image_file3 = save_picture(form.image_file3.data, 'portfolio_pics/' + folder_name, 900, 900)
        photo_image_file3 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file3)
        client_logo = save_picture(form.client_logo.data, 'portfolio_pics/' + folder_name, 900, 900)
        photo_client_logo = url_for('static', filename='portfolio_pics/' + folder_name + '/' + client_logo)

        user = User.query.first()
        portfolio = Portfolio(title=form.title.data, 
                            subtitle=form.subtitle.data, 
                            content=form.content.data, 
                            tag=form.tag.data,
                            image_file1=photo_image_file1, 
                            image_file2=photo_image_file2, 
                            image_file3=photo_image_file3, 
                            client_logo=photo_client_logo,
                            client_name=form.client_name.data) 

        db.session.add(portfolio)
        db.session.commit()
        return redirect(url_for('admin.admin_page'))

    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/portfolio-new.html', title='New portfolio', form=form, user=user, image_file=image_file)

@bp.route('/admin/portfolio/<int:portfolio_id>/update', methods=['POST', 'GET'])
@login_required
def portfolio_update(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    user = User.query.first()
    form = UpdatePortfolioForm()

    choiceList = [(choice.name, choice.name) for choice in Tag.query.all()]
    form.tag.choices = choiceList

    if form.validate_on_submit():

        folder_name = form.title.data
        directory = os.path.join(os.path.dirname(bp.root_path), 'static/', 'portfolio_pics/', folder_name)
        recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin')
        directory_recycle_bin = os.path.join(os.path.dirname(bp.root_path), 'static/recycle_bin/', folder_name)

        if os.path.exists(directory):
            if os.path.exists(directory_recycle_bin):
                shutil.rmtree(directory_recycle_bin)
            shutil.move(directory, recycle_bin)
            os.makedirs(directory)
        else:
            os.makedirs(directory)

        portfolio.title = form.title.data 
        portfolio.subtitle = form.subtitle.data
        portfolio.content = form.content.data 
        portfolio.date_posted = form.date_posted.data 
        portfolio.tag = form.tag.data
        portfolio.client_name = form.client_name.data

        #image_file is the input name
        if 'image_file1' in request.files:
            image_file1 = save_picture(form.image_file1.data, 'portfolio_pics/' + folder_name, 900, 900)
            photo_image_file1 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file1)
            portfolio.image_file1 = photo_image_file1
        if 'image_file1' in request.files:
            image_file2 = save_picture(form.image_file2.data, 'portfolio_pics/' + folder_name, 900, 900)
            photo_image_file2 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file2)
            portfolio.image_file2 = photo_image_file2
        if 'image_file1' in request.files:
            image_file3 = save_picture(form.image_file3.data, 'portfolio_pics/' + folder_name, 900, 900)
            photo_image_file3 = url_for('static', filename='portfolio_pics/' + folder_name + '/' + image_file3)
            portfolio.image_file3 = photo_image_file3
        if 'image_file1' in request.files:
            client_logo = save_picture(form.image_file1.data, 'portfolio_pics/' + folder_name, 900, 900)
            photo_client_logo = url_for('static', filename='portfolio_pics/' + folder_name + '/' + client_logo)
            portfolio.client_logo = photo_client_logo

        db.session.commit()
        return redirect(url_for('admin.admin_page'))

    elif request.method == 'GET':
        form.title.data = portfolio.title
        form.subtitle.data = portfolio.subtitle
        form.content.data = portfolio.content
        form.date_posted.data = portfolio.date_posted
        form.tag.data = portfolio.tag
        form.client_name.data = portfolio.client_name
        # if portfolio.image_file:
            # form.image_file = portfolio.image_file

    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/portfolio-update.html', 
                            title='Update Portfolio', 
                            user=user, 
                            image_file=user_image_file,
                            form=form, 
                            legend='Update Portfolio')
                            
@bp.route('/admin/portfolio/<int:portfolio_id>/delete', methods=['GET', 'POST'])
@login_required
def portfolio_delete(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    db.session.delete(portfolio)
    db.session.commit()
    return redirect(url_for('admin.admin_page'))

# tag
@bp.route('/admin/tag', methods=['GET', 'POST'])
def tag():
    user = User.query.first()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)

    form = TagForm()
    tags = Tag.query.all()
    if form.validate_on_submit():
        tag = Tag(name=form.tag_type.data)
        db.session.add(tag)
        db.session.commit()


        return redirect(url_for('admin.tag'))

    return render_template('admin/tag.html', title='tag', image_file=image_file, user=user, form=form, tags=tags) 

@bp.route('/admin/tag/<int:tag_id>/delete', methods=['GET', 'POST'])
@login_required
def tag_delete(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect(url_for('admin.tag'))

from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from forcewing import db
from forcewing.admin import bp
from forcewing.main.forms import LoginForm
from forcewing.admin.forms import CategoryForm, BlogForm, UpdateBlogForm
from forcewing.admin.forms import UpdateAccountInformationForm, UpdateAccountPhotoForm
from forcewing.admin.forms import TagForm, PortfolioForm, UpdatePortfolioForm
from forcewing.models import User, Blog, Category, Portfolio, Tag, PortfolioImage
from forcewing.func import save_picture, save_picture_port
import os, shutil

# admin

@bp.route('/admin/admin-page', methods=['POST', 'GET'])
@login_required
def admin_page():
    # form = LoginForm()
    user = User.query.first()
    blogs = Blog.query.order_by(Blog.date_posted.desc()).all()
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-page.html', title='Admin Page', image_file=user_image_file, user=user, blogs=blogs)

@bp.route('/admin/portfolio-page', methods=['POST', 'GET'])
@login_required
def portfolio_page():
    # form = LoginForm()
    user = User.query.first()
    portfolios = Portfolio.query.order_by(Portfolio.date_posted.desc()).all()
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/portfolio-page.html', title='Portfolio Page', image_file=user_image_file, user=user, portfolios=portfolios)

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
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-information.html', title='Update Account', image_file=user_image_file, form=form, user=user)

@bp.route('/admin/profile/photo', methods=['POST', 'GET'])
@login_required
def admin_update_photo():
    form = UpdateAccountPhotoForm()
    user = User.query.first()
    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'profile_pics', 130, 130)
            user.image_file = picture_file
        db.session.commit()
        return redirect(url_for('admin.admin_update_photo'))
        
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
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

        image_file = save_picture_port(form.image_file.data, 'blog_pics/')
        photo_image_file = url_for('static', filename='blog_pics/' + image_file)
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

    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: 
        user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-new.html', title='New Blog', form=form, user=user, image_file=user_image_file)

@bp.route('/admin/blog/<int:blog_id>/update', methods=['POST', 'GET'])
@login_required
def blog_update(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    user = User.query.first()
    form = UpdateBlogForm()

    choiceList = [(choice.name, choice.name) for choice in Category.query.all()]
    form.category.choices = choiceList

    if form.validate_on_submit():

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
            image_file = save_picture_port(form.image_file.data, 'blog_pics/')
            photo_image_file = url_for('static', filename='blog_pics/' + image_file)
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

    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: 
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
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    form = CategoryForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        category = Category(name=form.category_type.data)
        db.session.add(category)
        db.session.commit()

        return redirect(url_for('admin.category'))

    return render_template('admin/category.html', title='Category', image_file=user_image_file, user=user, form=form, categories=categories) 

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
        #logo image uploading
        logo_image = save_picture_port(form.logo_image.data, 'portfolio_pics/' )
        url_logo_image = url_for('static', filename='portfolio_pics/' + logo_image)

        #main image for showing in home page uploading
        main_image = save_picture_port(form.main_image.data, 'portfolio_pics/' )
        url_main_image = url_for('static', filename='portfolio_pics/' + main_image)

        #create the portfolio with all the information but the images
        portfolio = Portfolio(title=form.title.data, 
                            subtitle=form.subtitle.data, 
                            content=form.content.data, 
                            tag=form.tag.data,
                            client_name=form.client_name.data,
                            client_logo=url_logo_image,
                            main_image=url_main_image,
                            website=form.website.data,                            
                            user=user) 

        #retrieve the images
        requested_files_list = request.files.getlist('portfolio_images') # requested_files_list is a list of FileStorage
        if 'portfolio_images' in request.files:
            for one_file in requested_files_list: # one_file is FileStorage
                portfolio_image = save_picture_port(one_file, 'portfolio_pics/')
                portfolio_image_url = url_for('static', filename='portfolio_pics/' + portfolio_image)
                image = PortfolioImage(image=portfolio_image_url, portfolio=portfolio)
                db.session.add(image)

        
        db.session.add(portfolio)
        db.session.commit()
        return redirect(url_for('admin.portfolio_page'))

    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/portfolio-new.html', title='New portfolio', form=form, user=user, image_file=user_image_file)

@bp.route('/admin/portfolio/<int:portfolio_id>/update', methods=['POST', 'GET'])
@login_required
def portfolio_update(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    user = User.query.first()
    form = UpdatePortfolioForm()

    choiceList = [(choice.name, choice.name) for choice in Tag.query.all()]
    form.tag.choices = choiceList

    if form.validate_on_submit():
    
        
        portfolio.title = form.title.data 
        portfolio.subtitle = form.subtitle.data
        portfolio.content = form.content.data 
        portfolio.tag = form.tag.data
        portfolio.client_name = form.client_name.data
        portfolio.website = form.website.data
        #image_file is the input name
        if 'logo_image' in request.files:
            logo_image = save_picture_port(form.logo_image.data, 'portfolio_pics/')
            logo_image_url = url_for('static', filename='portfolio_pics/' + logo_image)
            portfolio.client_logo = logo_image_url
        if 'main_image' in request.files:
            main_image = save_picture_port(form.main_image.data, 'portfolio_pics/')
            main_image_url = url_for('static', filename='portfolio_pics/' + main_image)
            portfolio.main_image = main_image_url
        if 'portfolio_images' in request.files:
            requested_files_list = request.files.getlist('portfolio_images') # requested_files_list is a list of FileStorage
            if 'portfolio_images' in request.files:
                # delete old pictures from the database (replace functionality)
                for p_object in portfolio.portfolioimages:
                    db.session.delete(p_object)
                for one_file in requested_files_list: # one_file is FileStorage
                    portfolio_image = save_picture_port(one_file, 'portfolio_pics/')
                    portfolio_image_url = url_for('static', filename='portfolio_pics/' + portfolio_image)
                    image = PortfolioImage(image=portfolio_image_url, portfolio=portfolio)
                    db.session.add(image)
        db.session.commit()
        return redirect(url_for('admin.portfolio_page'))

    elif request.method == 'GET':
        form.title.data = portfolio.title
        form.subtitle.data = portfolio.subtitle
        form.content.data = portfolio.content
        form.tag.data = portfolio.tag
        form.client_name.data = portfolio.client_name
        form.website.data = portfolio.website

    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
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
    user_image_file = url_for('static', filename='myassets/logo/mylogodark.png')
    if user.image_file: user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    form = TagForm()
    tags = Tag.query.all()
    if form.validate_on_submit():
        tag = Tag(name=form.tag_type.data)
        tag.name_lower_case = tag.name.replace(" ", '_')
        db.session.add(tag)
        db.session.commit()

        return redirect(url_for('admin.tag'))

    return render_template('admin/tag.html', title='Tag', image_file=user_image_file, user=user, form=form, tags=tags) 

@bp.route('/admin/tag/<int:tag_id>/delete', methods=['GET', 'POST'])
@login_required
def tag_delete(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return redirect(url_for('admin.tag'))

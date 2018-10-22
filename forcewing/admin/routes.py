import secrets, os
from PIL import Image, ImageOps
from flask import render_template, redirect, url_for, request
from flask_login import login_required
from forcewing import db
from forcewing.admin import bp
from forcewing.main.forms import LoginForm
from forcewing.admin.forms import CategoryForm, BlogForm,  UpdateBlogForm, UpdateAccountInformationForm, UpdateAccountPhotoForm
from forcewing.models import User, Blog, Category

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
        if form.picture.data:
            picture_file = save_picture(form.picture.data, 'profile_pics', 130, 130)
            user.image_file = picture_file
        # user.username = form.username.data 
        db.session.commit()
        return redirect(url_for('admin.admin_update_photo'))
    user_image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/admin-update-photo.html', title='Update Account', image_file=user_image_file, form=form, user=user)

@bp.route('/admin/blog/new', methods=['POST', 'GET'])
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
        blog = Blog(title=form.title.data, content=form.content.data, quote=form.quote.data, 
                    image_file=photo_image_file, section_title=form.section_title.data, author=user, 
                    subsection_title=form.subsection_title.data,
                    subtitle=form.subtitle.data, category=form.category.data)

        db.session.add(blog)
        db.session.commit()
        return redirect(url_for('admin.admin_page'))

    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    return render_template('admin/blog-new.html', title='New Blog', form=form, user=user, image_file=image_file)

@bp.route('/admin/blog/<int:blog_id>/delete', methods=['GET', 'POST'])
@login_required
def blog_delete(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    db.session.delete(blog)
    db.session.commit()
    return redirect(url_for('admin.admin_page'))

@bp.route('/admin/blog/<int:blog_id>/update', methods=['POST', 'GET'])
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
            # image_to_be_deleted = blog.image_file 
            print('1 blog.image_file: ', blog.image_file)
            # blog.delete_images
            image_file = save_picture(form.image_file.data, 'blog_pics', 900, 900)
            photo_image_file = url_for('static', filename='blog_pics/' + image_file)
            blog.image_file = photo_image_file
            print('2 blog.image_file: ', blog.image_file)

        db.session.commit()
        return redirect(url_for('admin.admin_page'))

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

@bp.route('/admin/category/<int:category_id>/delete', methods=['GET', 'POST'])
@login_required
def category_delete(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for('admin.category'))

@bp.route('/admin/category', methods=['GET', 'POST'])
def category():
    user = User.query.first()
    image_file = url_for('static', filename='profile_pics/' + user.image_file)
    form = CategoryForm()
    categories = Category.query.all()
    if form.validate_on_submit():
        tag = Category(name=form.category_type.data)
        db.session.add(tag)
        db.session.commit()


        return redirect(url_for('admin.category'))

    return render_template('admin/category.html', title='Category', image_file=image_file, user=user, form=form, categories=categories) 

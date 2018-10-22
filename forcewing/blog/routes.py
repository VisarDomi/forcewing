from flask import render_template, request
from forcewing import db
from forcewing.blog import bp
from forcewing.main.forms import LoginForm
from forcewing.models import Blog, Category

# blog
def change_text(id):
    blog = Blog.query.filter_by(id=id).first()
    lines = blog.content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

# blog

@bp.route('/bloglist', methods=['GET', 'POST'])
def bloglist():
    blogs = Blog.query.paginate(per_page=5)
    categories = Category.query.all()
    loginForm = LoginForm()

    return render_template('blog/bloglist.html', loginForm=loginForm, title='Blog posts', blogs=blogs, categories=categories)

@bp.route('/blog/<int:blog_id>', methods=['GET', 'POST'])
def blog(blog_id):
    blog = Blog.query.get_or_404(blog_id)
    returnedHtml = change_text(blog_id)
    loginForm = LoginForm()
    # paragraph = blog.content

    return render_template('blog/blog.html', title=blog.title, blog=blog, loginForm=loginForm, returnedHtml=returnedHtml)

@bp.route('/blog/<string:category>')
def filtered_blogs(category):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    categories = Category.query.all()
    blogs = Blog.query.filter_by(category=category)\
            .order_by(Blog.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('blog/blog-category.html', form=form, title=category, category=category, blogs=blogs, categories=categories)


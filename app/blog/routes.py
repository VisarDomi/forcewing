from flask import render_template, request
from app.blog import bp
from app.main.forms import LoginForm
from app.models import Blog, Category
from app.func import change_text_section_content, change_text_subsection_content

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
    section_content_paragraphs = change_text_section_content(blog_id)
    paragraph_one = section_content_paragraphs.pop(0)
    subsection_content_paragraphs = change_text_subsection_content(blog_id)
    loginForm = LoginForm()

    return render_template('blog/blog.html', 
                            title=blog.title, 
                            blog=blog, 
                            loginForm=loginForm, 
                            paragraph_one=paragraph_one, 
                            section_content_paragraphs=section_content_paragraphs,
                            subsection_content_paragraphs=subsection_content_paragraphs)

@bp.route('/blog/<string:category>')
def filtered_blogs(category):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    categories = Category.query.all()
    blogs = Blog.query.filter_by(category=category)\
            .order_by(Blog.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('blog/blog-category.html', form=form, title=category, category=category, blogs=blogs, categories=categories)


from flask import render_template
from forcewing.portfolio import bp
from forcewing.main.forms import LoginForm
from forcewing.models import Category, Portfolio

# portfolio
def change_text_portfolio(id):
    portfolio = Portfolio.query.filter_by(id=id).first()
    lines = portfolio.content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

# portfolio

@bp.route('/bloglist', methods=['GET', 'POST'])
def bloglist():
    blogs = Blog.query.paginate(per_page=5)
    categories = Category.query.all()
    loginForm = LoginForm()

    return render_template('blog/bloglist.html', loginForm=loginForm, title='Blog posts', blogs=blogs, categories=categories)

@bp.route('/portfolio/<int:portfolio_id>', methods=['GET', 'POST'])
def portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    returnedHtml = change_text_portfolio(portfolio_id)
    loginForm = LoginForm()

    return render_template('blog/portfolio.html', title=portfolio.title, portfolio=portfolio, loginForm=loginForm, returnedHtml=returnedHtml)

@bp.route('/blog/<string:category>')
def filtered_blogs(category):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    categories = Category.query.all()
    blogs = Blog.query.filter_by(category=category)\
            .order_by(Blog.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('blog/blog-category.html', form=form, title=category, category=category, blogs=blogs, categories=categories)

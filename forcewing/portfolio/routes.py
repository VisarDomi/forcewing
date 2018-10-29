from flask import render_template, request
from forcewing.portfolio import bp
from forcewing.main.forms import LoginForm
from forcewing.models import Portfolio, Tag
from forcewing.func import change_text_content


# portfolio

@bp.route('/portfoliolist', methods=['GET', 'POST'])
def portfoliolist():
    portfolios = Portfolio.query.paginate(per_page=5)
    tags = Tag.query.all()
    loginForm = LoginForm()

    return render_template('portfolio/portfoliolist.html', loginForm=loginForm, title='Portfolio posts', portfolios=portfolios, tags=tags)

@bp.route('/portfolio/<int:portfolio_id>', methods=['GET', 'POST'])
def portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    portfolio_images = portfolio.portfolioimages
    content_paragraphs = change_text_content(portfolio_id)
    loginForm = LoginForm()

    return render_template('portfolio/portfolio.html', 
                            title=portfolio.title, 
                            portfolio=portfolio, 
                            portfolio_images=portfolio_images,
                            loginForm=loginForm, 
                            content_paragraphs=content_paragraphs)

@bp.route('/portfolio/<string:tag>')
def filtered_portfolios(tag):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    tags = Tag.query.all()
    portfolios = Portfolio.query.filter_by(tag=tag)\
            .order_by(Portfolio.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('portfolio/portfolio-tag.html', form=form, title=tag, tag=tag, portfolios=portfolios, tags=tags)


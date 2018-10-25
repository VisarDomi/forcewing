from flask import render_template, request
from forcewing.portfolio import bp
from forcewing.main.forms import LoginForm
from forcewing.models import Portfolio, Tag

# portfolio
def change_text_section_content(id):
    portfolio = Portfolio.query.filter_by(id=id).first()
    lines = portfolio.section_content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

def change_text_subsection_content(id):
    portfolio = Portfolio.query.filter_by(id=id).first()
    lines = portfolio.subsection_content.split('\r\n\r\n')
    html=[]
    for text in lines:
        if text:
            string = str(text)
            html.append(string)
    return html

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
    section_content_paragraphs = change_text_section_content(portfolio_id)
    paragraph_one = section_content_paragraphs.pop(0)
    subsection_content_paragraphs = change_text_subsection_content(portfolio_id)
    loginForm = LoginForm()

    return render_template('portfolio/portfolio.html', 
                            title=portfolio.title, 
                            portfolio=portfolio, 
                            loginForm=loginForm, 
                            paragraph_one=paragraph_one, 
                            section_content_paragraphs=section_content_paragraphs,
                            subsection_content_paragraphs=subsection_content_paragraphs)

@bp.route('/portfolio/<string:tag>')
def filtered_portfolios(tag):
    page = request.args.get('page', 1, type=int)
    form = LoginForm()
    tags = Tag.query.all()
    portfolios = Portfolio.query.filter_by(tag=tag)\
            .order_by(Portfolio.date_posted.desc())\
            .paginate(page=page, per_page=5)
    return render_template('portfolio/portfolio-tag.html', form=form, title=tag, tag=tag, portfolios=portfolios, tags=tags)


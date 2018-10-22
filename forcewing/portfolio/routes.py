from flask import render_template
from forcewing.portfolio import bp
from forcewing.main.forms import LoginForm
from forcewing.models import Category

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

@bp.route('/portfolio/<int:portfolio_id>', methods=['GET', 'POST'])
def portfolio(portfolio_id):
    portfolio = Portfolio.query.get_or_404(portfolio_id)
    returnedHtml = change_text_portfolio(portfolio_id)
    loginForm = LoginForm()

    return render_template('blog/portfolio.html', title=portfolio.title, portfolio=portfolio, loginForm=loginForm, returnedHtml=returnedHtml)

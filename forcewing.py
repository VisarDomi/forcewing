from forcewing import create_app, db
from forcewing.models import User, Category, Blog, Portfolio, Tag, PortfolioImage

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'User': User,
            'Category': Category,
            'Blog': Blog,
            'PortfolioImage':PortfolioImage,
            'Portfolio': Portfolio,
            'Tag': Tag}
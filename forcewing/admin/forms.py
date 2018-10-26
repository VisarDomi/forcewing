from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from forcewing.models import Category, Tag

# admin

class UpdateAccountInformationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Update Account')

class UpdateAccountPhotoForm(FlaskForm):
    picture = FileField('Update Profile picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update Account')

#blog
class CategoryForm(FlaskForm):
    category_type = StringField('Category', validators=[DataRequired()])
    submit = SubmitField('Create Category')

    def validate_category_type(self, category_type):
        category = Category.query.filter_by(name=category_type.data).first()
        if category:
            raise ValidationError('That category is taken. Please choose a different one.')

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    section_title = StringField('Section Title')
    section_content = TextAreaField('Section Content')
    subsection_title = StringField('Subsection Title')
    subsection_content = TextAreaField('Subsection Content')
    quote = StringField('Quote')
    category = SelectField('Category', choices=[])
    image_file = FileField('Photo', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    submit = SubmitField('Create Blog')

class UpdateBlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    section_title = StringField('Section Title')
    section_content = TextAreaField('Section Content')
    subsection_title = StringField('Subsection Title')
    subsection_content = TextAreaField('Subsection Content')
    quote = StringField('Quote')
    category = SelectField('Category', choices=[])
    image_file = FileField('Photo', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    submit = SubmitField('Update Blog')

#portfolio
class TagForm(FlaskForm):
    tag_type = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Create Tag')

    def validate_tag_type(self, tag_type):
        tag = Tag.query.filter_by(name=tag_type.data).first()
        if tag:
            raise ValidationError('That tag is taken. Please choose a different one.')

class PortfolioForm(FlaskForm):
    date_posted = DateField('Date Posted (optional, default=datetime.utcnow)')
    title = StringField('Portfolio Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    content = TextAreaField('Portfolio Content')
    tag = SelectField('Tag', choices=[])
    image_file = FileField('Client Logo', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    client_name = StringField('Client Name')
    website = StringField('Website')
    submit = SubmitField('Create Portfolio')

class UpdatePortfolioForm(FlaskForm):
    date_posted = DateField('Date Posted (optional, default=datetime.utcnow)')
    title = StringField('Portfolio Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    content = TextAreaField('Portfolio Content')
    tag = SelectField('Tag', choices=[])
    image_file = FileField('Client Logo', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    client_name = StringField('Client Name')
    website = StringField('Website')
    submit = SubmitField('Update Portfolio')

class ImagesPortfolioForm(FlaskForm):
    image_file = FileField('Photo', validators=[FileAllowed(['png', 'jpg', 'jpeg'])])
    submit = SubmitField('Update Portfolio')

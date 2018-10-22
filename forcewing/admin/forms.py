from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from forcewing.models import Category

# admin

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
    content = TextAreaField('Blog Content', validators=[DataRequired()])
    section_title = StringField('Section Title')
    subsection_title = StringField('Subsection Title')
    quote = StringField('Quote')
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    image_file = FileField('Photo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    submit = SubmitField('Create Blog')

class UpdateBlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    section_title = StringField('Section Title', validators=[DataRequired()])
    subsection_title = StringField('Subsection Title', validators=[DataRequired()])
    quote = StringField('Quote', validators=[DataRequired()])
    content = TextAreaField('Blog Content', validators=[DataRequired()])
    image_file = FileField('Photo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    submit = SubmitField('Update Blog')

class UpdateAccountInformationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Update Account')

class UpdateAccountPhotoForm(FlaskForm):
    picture = FileField('Update Profile picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update Account')

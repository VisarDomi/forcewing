from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from flask_wtf.file import FileField, FileAllowed
from forcewing.models import Category 




class LoginForm(FlaskForm):
    username = StringField('Login', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submitLogin = SubmitField('Log In')

class BlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    subtitle = StringField('Blog Subtitle', validators=[DataRequired()])
    big_quote =  StringField('Big Quote', validators=[DataRequired()])
    big_quote_author =  StringField('Big Quote Author', validators=[DataRequired()])
    small_quote =  StringField('Small Quote', validators=[DataRequired()])
    content =  TextAreaField('Blog Content', validators=[DataRequired()])
    image_file = FileField('Photo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    submit = SubmitField('Create blog')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone')
    subject =  StringField('Subject', validators=[DataRequired()])
    message =  TextAreaField('Message', validators=[DataRequired()])
    submitContact = SubmitField('Send')

class UpdateAccountInformationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Update Account')

class UpdateAccountPhotoForm(FlaskForm):
    picture = FileField('Update Profile picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Update Account')

class UpdateBlogForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired()])
    subtitle = StringField('Blog Subtitle', validators=[DataRequired()])
    big_quote =  StringField('Big Quote', validators=[DataRequired()])
    big_quote_author =  StringField('Big Quote Author', validators=[DataRequired()])
    small_quote =  StringField('Small Quote', validators=[DataRequired()])
    content =  TextAreaField('Blog Content', validators=[DataRequired()])
    image_file = FileField('Photo', validators=[FileAllowed(['png', 'jpg'])])
    category = SelectField('Category', choices=[], validators=[DataRequired()])
    submit = SubmitField('Update Blog')

class CategoryForm(FlaskForm):
    category_type = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_category_type(self, category_type):
        category = Category.query.filter_by(name=category_type.data).first()
        if category:
            raise ValidationError('That category is taken. Please choose a different one')


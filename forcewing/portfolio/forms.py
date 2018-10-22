from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField, DateField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed
from forcewing.models import Category, Tag

# portfolio

class TagForm(FlaskForm):
    tag_type = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Create')

    def validate_category_type(self, tag_type):
        tag = Tag.query.filter_by(name=tag_type.data).first()
        if tag:
            raise ValidationError('That tag is taken. Please choose a different one.')

class PortfolioForm(FlaskForm):
    title = StringField('Portfolio Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    content = TextAreaField('Portfolio Content', validators=[DataRequired()])
    date_posted = DateField('Date Posted')
    tag = SelectField('Tag', choices=[], validators=[DataRequired()])
    image_file = FileField('Photo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    client_logo = FileField('Client Logo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    client_name = StringField('Client Name', validators=[DataRequired()])
    submit = SubmitField('Create Portfolio')

class UpdatePortfolioForm(FlaskForm):
    title = StringField('Portfolio Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle')
    content = TextAreaField('Portfolio Content', validators=[DataRequired()])
    date_posted = DateField('Date Posted')
    tag = SelectField('Tag', choices=[], validators=[DataRequired()])
    image_file = FileField('Photo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    client_logo = FileField('Client Logo', validators=[DataRequired(), FileAllowed(['png', 'jpg', 'jpeg'])])
    client_name = StringField('Client Name', validators=[DataRequired()])
    submit = SubmitField('Update Portfolio')

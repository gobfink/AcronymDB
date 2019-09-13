# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Tag

class TagsForm(FlaskForm):
    """
    Form for admin to add or edit tags
    """
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Submit')

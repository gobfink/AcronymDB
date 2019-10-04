# app/home/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Acronym

class AcronymsForm(FlaskForm):
    """
    Form for  adding or editing acronym
    """
    acronym = StringField('Acronym', validators=[DataRequired()])
    definition = StringField('Definition', validators=[DataRequired()])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')


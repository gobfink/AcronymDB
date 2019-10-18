# app/home/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, Form, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Acronym

def _required(form, field):
    if not field.raw_data or not field.raw_data[0]:
       raise ValidationError('Field is required') 

class AcronymsForm(FlaskForm):
    """
    Form for  adding or editing acronym
    """
    acronym = StringField('Acronym', validators=[_required, Length(1, 80)])
    definition = StringField('Definition', validators=[_required, Length(1, 80)])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

class AcronymSearchForm(Form):
    choices = [('acronym', 'Acronym'),
               ('definition','Definition'),
               ('tag','Tags')]
    select = SelectField('',choices=choices)
    search = StringField('')


class AddTagForm(FlaskForm):
    choices=[]
    select = SelectField('Tag to Add',choices=choices, validators=[DataRequired()])
    submit = SubmitField('Submit')
    cancel = SubmitField('Cancel')

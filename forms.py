from flask_wtf import FlaskForm
from wtforms import (StringField)
from wtforms.validators import InputRequired, Length


class CourseForm(FlaskForm):
    crn1 = StringField('crn1', validators=[InputRequired(), Length(min=5, max=5)])
    crn2 = StringField('crn2', validators=[Length(min=0, max=5)])
    crn3 = StringField('crn3', validators=[Length(min=0, max=5)])
    crn4 = StringField('crn4', validators=[Length(min=0, max=5)])
    crn5 = StringField('crn5', validators=[Length(min=0, max=5)])
    crn6 = StringField('crn6', validators=[Length(min=0, max=5)])

__author__ = 'kwhatcher'

from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class AlertForm(Form):
    msg = StringField('msg', validators=[DataRequired()])
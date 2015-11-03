__author__ = 'kwhatcher'


from flask_wtf import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired



class ContactForm(Form):
    phone = StringField('Phone Number', validators=[DataRequired()])



__author__ = 'kwhatcher'


from flask_wtf import Form
from wtforms import StringField
from wtforms import SelectField
from wtforms.validators import DataRequired

from SDFtools.models import gawxstations


class ContactForm(Form):
    phone = StringField('Phone Number', validators=[DataRequired()])


class SettingsForm(Form):
    #wxstation = StringField('WX Station', validators=[DataRequired()])
    gastations = gawxstations()
    options = [(wx, gastations[wx]) for wx in gastations]

    print options
    wxstation = SelectField(u'Programming Language', choices=options)
    #language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
__author__ = 'kwhatcher'

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask.ext.stormpath import login_required, user
from flask import render_template_string
import boto

from SDFtools.forms import MyForm

boto.set_stream_logger('boto')

gui = Blueprint('gui', __name__)

@gui.route('/')
@login_required
def hello_world():
    return render_template('test.html', form=MyForm())

@gui.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        sns = boto.connect_sns()
        msg = "Hi there\nI am sending this message over boto.\nYour booty Jan"
        subj = form.data['msg']

        res = sns.publish("arn:aws:sns:us-east-1:150179862823:5bde_alerts", msg, subj)
        return redirect('/success')
    return render_template('submit.html', form=form)

@gui.route('/success')
def success():
    return render_template('success.html', form=MyForm())
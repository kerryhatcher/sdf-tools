__author__ = 'kwhatcher'

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import flash
from flask.ext.stormpath import login_required, user
from flask import render_template_string
import boto
from flask.ext import menu
import  pywapi

from SDFtools.forms import MyForm

boto.set_stream_logger('boto')

gui = Blueprint('gui', __name__)
noaa_result = pywapi.get_weather_from_noaa('KLSF')

@gui.route('/')
@menu.register_menu(gui, 'Home', 'Dashboard')
@login_required
def hello_world():
    return render_template('base.html', weather=noaa_result)

@gui.route('/alert')
@menu.register_menu(gui, 'Send Alert', 'Send Alert')
@login_required
def send_alert():
    return render_template('alert.html', form=MyForm())

@gui.route('/submit', methods=('GET', 'POST'))
@login_required
def submit():
    form = MyForm()
    if form.validate_on_submit():
        sns = boto.connect_sns()
        msg = "Hi there\nI am sending this message over boto.\nYour booty Jan"
        subj = form.data['msg']

        #res = sns.publish("arn:aws:sns:us-east-1:150179862823:5bde_alerts", msg, subj)
        flash('Message Sent')
        return redirect('/alert')
    return render_template('submit.html', form=form)

@gui.route('/success')
@login_required
def success():
    return render_template('success.html', form=MyForm())


@gui.route('/settings')
@login_required
def settings():
    return render_template('settings.html')

@gui.route('/profile')
@login_required
def profile():
    return render_template('profile.html', user=user)

@gui.route('/help')
@login_required
def help():
    return render_template('help.html')
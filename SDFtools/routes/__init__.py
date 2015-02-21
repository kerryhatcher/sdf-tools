__author__ = 'kwhatcher'

from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import flash
import boto
from flask.ext import menu
from flask.ext.cors import cross_origin
from flask import session

from SDFtools.auth.decorators import requires_auth
from SDFtools.forms import AlertForm
from SDFtools.forms.user import ContactForm
from SDFtools.forms.user import SettingsForm
from SDFtools.models import gawxstations
from SDFtools.models.user import setuserwx
from SDFtools.models import missions



boto.set_stream_logger('boto')

gui = Blueprint('gui', __name__)

sns = boto.connect_sns()
snstopic_arn = "arn:aws:sns:us-east-1:150179862823:5bde_alerts"

@gui.route('/')
@menu.register_menu(gui, 'Home', 'Dashboard')
@requires_auth
def hello_world():
    return render_template('base.html')

@gui.route('/alert')
@menu.register_menu(gui, 'Send Alert', 'Send Alert')
@requires_auth
def send_alert():
 
    subscriptions = sns.get_all_subscriptions_by_topic(snstopic_arn)
    return render_template('alert.html', form=AlertForm(), subscriptions=subscriptions  )

@gui.route('/submit', methods=('GET', 'POST'))
@requires_auth
def submit():
 
    form = AlertForm()
    if form.validate_on_submit():

        msg = "Hi there\nI am sending this message over boto.\nYour booty Jan"
        subj = form.data['msg']

        res = sns.publish(snstopic_arn, msg, subj)
        flash('Message Sent')
        return redirect('/alert')
    return render_template('submit.html', form=form)

@gui.route('/success')
@requires_auth
def success():
 
    return render_template('success.html', form=AlertForm() )


@gui.route('/settings')
@requires_auth
def settings():

    return render_template('settings.html', user=session['profile'], form=SettingsForm())

@gui.route('/settings/submit', methods=('GET', 'POST'))
@requires_auth
def settingssubmit():
    form = SettingsForm()
    if form.validate_on_submit():
        flash('Data Received')
        station = form.data['wxstation']
        print station
        setuserwx(station)
        return redirect('/settings')
    flash('Data error')
    return render_template('settings.html', user=session['profile'], form=SettingsForm())

@gui.route('/profile')
@requires_auth
def profile():
    print "PROFILE TEST"
    return render_template('profile.html', user=session['profile'], contactform=ContactForm())

# This does need authentication
@gui.route("/secured/ping")
@cross_origin(headers=['Content-Type', 'Authorization'])
@requires_auth
def securedPing():
    return "All good. You only get this message if you're authenticated"

@gui.route('/profile/submit', methods=('GET', 'POST'))
@requires_auth
def profilesubmit():
 
    form = ContactForm()
    if form.validate_on_submit():
        user = session['profile']
        user.custom_data['phone'] = form.data['phone']
        user.save()
        print('User Data:')
        print user.custom_data['phone']
        flash('Data Received')
        return redirect('/profile')
    return render_template('profile.html', contactform=ContactForm())

@gui.route('/help')
@requires_auth
def help():
    return render_template('help.html' )


""" Missions Tracker """

@gui.route('/missions')
@menu.register_menu(gui, 'missiontracker', 'Mission Tracker')
@requires_auth
def missionsroot():
    data = missions.getallmissions()
    urls = []
    for item in data:
        #print "##################SAD TESTINGS#############################"
        #print item['SAD_ID']
        url = missions.getmissionurl(item['SAD_ID'])
        #print url
        urls.append(url)

    print urls
    return render_template('missions.html', data=data, urls=urls)

""" BluTrac """

@gui.route('/blutrac')
@menu.register_menu(gui, 'blutrac', 'Troop Tracker')
@requires_auth
def trackerroot():
    #data = missions.getallmissions()
    return render_template('blutrac.html')


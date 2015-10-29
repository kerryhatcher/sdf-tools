__author__ = 'kwhatcher'

from flask import Blueprint, request
import twilio.twiml

phone = Blueprint('phone', __name__)




@phone.route("/sms", methods=['GET', 'POST'])
def hello_sms():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)



    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)


@phone.route("/voice", methods=['GET', 'POST'])
def hello_voice():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Monkey")

    return str(resp)
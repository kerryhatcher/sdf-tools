__author__ = 'kwhatcher'

from flask import Blueprint
import twilio.twiml

phone = Blueprint('phone', __name__)




@phone.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""

    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

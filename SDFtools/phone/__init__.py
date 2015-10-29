__author__ = 'kwhatcher'

from flask import Blueprint, request
import twilio.twiml
from twilio.rest import TwilioRestClient
from os import environ
from flask import url_for
from elasticsearch import Elasticsearch



es = Elasticsearch([environ.get('ES_CONNECT_STRING')])


phone = Blueprint('phone', __name__)

# Find these values at https://twilio.com/user/account
account_sid = environ.get('TWILIO_ACCOUNT_SID')
auth_token = environ.get('TWILIO_AUTH_TOKEN')
client = TwilioRestClient(account_sid, auth_token)


@phone.route("/sms", methods=['GET', 'POST'])
def hello_sms():
    """Respond to incoming calls with a simple text message."""
    from_number = request.values.get('From', None)

    resp = twilio.twiml.Response()
    resp.message("Roger")
    return str(resp)

@phone.route("/sms_sendmessage", methods=['GET'])
def send_sms():
    """Send a message to someone"""
    to_number = "+1 " + request.args.get('number')

    message = client.messages.create(to=to_number, from_="+14782922959",
                                     body=request.args.get('message'))

    return "<h1>SENT</h1>"


@phone.route("/voice", methods=['GET', 'POST'])
def hello_voice():
    """Respond to incoming requests."""
    resp = twilio.twiml.Response()
    resp.say("Hello Soldier, get back to work")

    return str(resp)


@phone.route("/voice/call", methods=['GET'])
def send_voice():
    """make a call."""
    to_number = "+1 " + request.args.get('number')
    call = client.calls.create(to=to_number,
                               from_="+14782922959",
                                url='https://gsdf5th.herokuapp.com/phone/voice')
    return "<h1>SENT</h1>"


@phone.route("/numbers/add", methods=['GET'])
def add_numbers():
    doc = {
    'name': request.args.get('name'),
    'number': request.args.get('number'),
    }
    res = es.index(index="phonebook", doc_type='phonenumber', id=request.args.get('number'), body=doc)
    return res['created']

@phone.route("/number", methods=['GET'])
def get_number():
    res = es.get(index="phonebook", doc_type='phonenumber', id=request.args.get('number'))

    return res['_source']

@phone.route("/numbers", methods=['GET'])
def get_numbers():
    res = es.search(index="test-index", body={"query": {"match_all": {}}})
    return res['hits']['hits']

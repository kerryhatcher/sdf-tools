__author__ = 'kwhatcher'

from flask import Blueprint


phone = Blueprint('phone', __name__)


@phone.route('/')
def hello_world():
    return "hello world"
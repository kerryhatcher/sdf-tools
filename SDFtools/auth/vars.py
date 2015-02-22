__author__ = 'kwhatcher'
from os import environ


client_id = environ.get('AUTH0_CLIENT_ID'),
client_secret = environ.get('AUTH0_CLIENT_SECRET'),
redirect_uri = environ.get('AUTH0_CALLBACK_URL'),
grant_type = 'authorization_code'

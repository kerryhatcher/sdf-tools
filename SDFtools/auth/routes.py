__author__ = 'kwhatcher'

__author__ = 'kwhatcher'


import os
import json

import requests
from flask import request, session, redirect, render_template
from flask import Blueprint
from os import environ


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


# Here we're using the /callback route.
@auth.route('/callback')
def callback_handling():
    env = os.environ
    code = request.args.get('code')

    json_header = {'content-type': 'application/json'}

    token_url = "https://{domain}/oauth/token".format(domain=environ.get('AUTH0_DOMAIN'))

    token_payload = {
    'client_id':     environ.get('AUTH0_CLIENT_ID'),
    'client_secret': environ.get('AUTH0_CLIENT_SECRET'),
    'redirect_uri':  environ.get('AUTH0_CALLBACK_URL'),
    'code':          code,
    'grant_type':    'authorization_code'
  }

    token_info = requests.post(token_url, data=json.dumps(token_payload), headers = json_header).json()
    print token_info

    user_url = "https://{domain}/userinfo?access_token={access_token}" \
      .format(domain='app33477067.auth0.com', access_token=token_info['access_token'])

    user_info = requests.get(user_url).json()

  # We're saving all user information into the session
    session['profile'] = user_info

  # Redirect to the User logged in page that you want here
  # In our case it's /dashboard
    return redirect('/profile')
__author__ = 'kwhatcher'

import jwt
import base64
import os

from functools import wraps
from flask import Flask, request, jsonify, _request_ctx_stack, current_app, session, redirect
from werkzeug.local import LocalProxy
from flask.ext.cors import cross_origin

app = current_app

# Authentication annotation
current_user = LocalProxy(lambda: _request_ctx_stack.top.current_user)

# Authentication attribute/annotation
def authenticate(error):
  resp = jsonify(error)

  resp.status_code = 401

  return resp

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    if not session.has_key('profile'):
      # Redirect to Login page here
      return redirect('/login')
    return f(*args, **kwargs)

  return decorated

def api_requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.headers.get('Authorization', None)
    if not auth:
      return authenticate({'code': 'authorization_header_missing', 'description': 'Authorization header is expected'})

    parts = auth.split()

    if parts[0].lower() != 'bearer':
      return {'code': 'invalid_header', 'description': 'Authorization header must start with Bearer'}
    elif len(parts) == 1:
      return {'code': 'invalid_header', 'description': 'Token not found'}
    elif len(parts) > 2:
      return {'code': 'invalid_header', 'description': 'Authorization header must be Bearer + \s + token'}

    token = parts[1]
    try:
        payload = jwt.decode(
            token,
            base64.b64decode('IwL6HLt8Ta4D_YWKv9WfNqc1LElJsjnus2YgyrG9xTITHD4sqGq1j82Slz59gtvM'.replace("_","/").replace("-","+"))
        )
    except jwt.ExpiredSignature:
        return authenticate({'code': 'token_expired', 'description': 'token is expired'})
    except jwt.DecodeError:
        return authenticate({'code': 'token_invalid_signature', 'description': 'token signature is invalid'})

    if payload['aud'] != '5xNV1SekE1QjPXFz8UH7PUayx3PpILec':
      return authenticate({'code': 'invalid_audience', 'description': 'the audience does not match. expected: ' + CLIENT_ID})

    _request_ctx_stack.top.current_user = user = payload
    return f(*args, **kwargs)

  return decorated


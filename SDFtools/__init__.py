__author__ = 'kwhatcher'


from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext import menu
from os import environ





from routes import gui
from SDFtools.auth.routes import auth
from cache import cache
from SDFtools.api import api
from SDFtools import weather
from SDFtools import gmaps
from SDFtools.auth import context as authcontext




app = Flask(__name__)

app.register_blueprint(gui)
app.register_blueprint(auth)

Bootstrap(app)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')

authcontext.Auth(app=app)
menu.Menu(app=app)
weather.Weather(app=app)
gmaps.Gmap(app=app)








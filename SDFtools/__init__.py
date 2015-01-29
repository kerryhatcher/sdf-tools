__author__ = 'kwhatcher'


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from os.path import expanduser
from flask.ext.stormpath import StormpathManager
from flask.ext import menu
from os import environ
from SDFtools import weather
import ast
from flask.ext.cache import Cache




from routes import gui
from cache import cache




app = Flask(__name__)
app.register_blueprint(gui)
Bootstrap(app)
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)
#app.config['SECRET_KEY'] = "734yt98473yt734ytc98y3tn98y897r67no"
#app.config['STORMPATH_API_KEY_FILE'] = expanduser('~/.stormpath')

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['STORMPATH_API_KEY_ID'] = environ.get('STORMPATH_API_KEY_ID')
app.config['STORMPATH_API_KEY_SECRET'] = environ.get('STORMPATH_API_KEY_SECRET')

app.config['STORMPATH_APPLICATION'] = 'gsdf5th'
#app.config['STORMPATH_ENABLE_GOOGLE'] = True
#app.config['STORMPATH_SOCIAL'] = ast.literal_eval(environ.get('STROMPATH-SOCIAL'))


app.config['STORMPATH_LOGIN_TEMPLATE'] = 'login.html'

stormpath_manager = StormpathManager(app)
menu.Menu(app=app)

weather.Weather(app=app)

if __name__ == '__main__':
    app.run(debug=True)




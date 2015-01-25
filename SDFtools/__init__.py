__author__ = 'kwhatcher'


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from os.path import expanduser
from flask.ext.stormpath import StormpathManager
from flask.ext import menu
from os import environ
from routes import gui

app = Flask(__name__)
app.register_blueprint(gui)
Bootstrap(app)

#app.config['SECRET_KEY'] = "734yt98473yt734ytc98y3tn98y897r67no"
#app.config['STORMPATH_API_KEY_FILE'] = expanduser('~/.stormpath')

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['STORMPATH_API_KEY_ID'] = environ.get('STORMPATH_API_KEY_ID')
app.config['STORMPATH_API_KEY_SECRET'] = environ.get('STORMPATH_API_KEY_SECRET')

app.config['STORMPATH_APPLICATION'] = 'gsdf5th'
app.config['STORMPATH_ENABLE_GOOGLE'] = True
app.config['STORMPATH_SOCIAL'] = environ.get('STROMPATH-SOCIAL')


stormpath_manager = StormpathManager(app)
menu.Menu(app=app)



if __name__ == '__main__':
    app.run(debug=True)




__author__ = 'kwhatcher'


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from os.path import expanduser
from flask.ext.stormpath import StormpathManager
from flask.ext import menu
from routes import gui
from os import environ

app = Flask(__name__)
app.register_blueprint(gui)
Bootstrap(app)

app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
app.config['STORMPATH_API_KEY_ID'] = environ.get('STORMPATH_API_KEY_ID')
app.config['STORMPATH_API_KEY_SECRET'] = environ.get('STORMPATH_API_KEY_SECRET')
app.config['STORMPATH_APPLICATION'] = environ.get('STORMPATH_URL')


stormpath_manager = StormpathManager(app)
menu.Menu(app=app)



if __name__ == '__main__':
    app.run(debug=True)




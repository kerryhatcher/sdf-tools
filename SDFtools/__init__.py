__author__ = 'kwhatcher'


from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from os.path import expanduser
from flask.ext.stormpath import StormpathManager

from routes import gui

app = Flask(__name__)
app.register_blueprint(gui)
Bootstrap(app)

app.config['SECRET_KEY'] = "734yt98473yt734ytc98y3tn98y897r67no"
app.config['STORMPATH_API_KEY_FILE'] = expanduser('apiKey.properties')
app.config['STORMPATH_APPLICATION'] = 'GSDF'


stormpath_manager = StormpathManager(app)




if __name__ == '__main__':
    app.run(debug=True)




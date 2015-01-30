__author__ = 'kwhatcher'

from . import app

@app.route('/search', subdomain='api')
def api_search():
    pass
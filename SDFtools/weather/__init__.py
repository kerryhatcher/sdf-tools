__author__ = 'kwhatcher'

"""Provide support for generating weather info for use in templates

Depends on 'pywapi'
"""

import pywapi
from werkzeug.local import LocalProxy
from flask.ext.stormpath import user

class Weather(object):

    def __init__(self, app):
        if app is not None:
            self.init_app(app)

    def init_app(self, app, *args, **kwargs):
        app.context_processor(Weather.weather_context_processor)

        self.app = app
        if not hasattr(app, 'extensions'):
            app.extensions = {}




    @staticmethod
    def weather():
        """Backend function for weather proxy

        :return: A list of weather items
        """
        # Construct weather
        weather_list = pywapi.get_weather_from_noaa(user.custom_data['wx'])

        return weather_list

    @staticmethod
    def weather_context_processor():
        """add variable ''weather'' to template context

        It contains the list of weather entries to render as a widget
        """

        return dict(weather2=current_weather)





#: A proxy for current weather list.
current_weather = LocalProxy(Weather.weather)
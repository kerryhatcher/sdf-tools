__author__ = 'kwhatcher'
from flask.ext.stormpath import user
from SDFtools.cache import cache
import  pywapi

def setuserwx(station):
    user.custom_data['wx'] = station
    user.save()

def getuserwxstation():
    return user.custom_data['wx']

#@cache.cached(30, key_prefix='get_wx')
def getuserwx():
    userstation = getuserwxstation()
    print userstation
    noaa_result = pywapi.get_weather_from_noaa(userstation)
    print noaa_result
    return noaa_result
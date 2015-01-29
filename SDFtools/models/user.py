__author__ = 'kwhatcher'
from flask.ext.stormpath import user
from SDFtools.cache import cache
import  pywapi

def setuserwx(station):
    user.custom_data['wx'] = station
    user.save()

def getuserwxstation():
    return user.custom_data['wx']


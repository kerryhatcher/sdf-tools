__author__ = 'kwhatcher'


from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table
import inspect
import json

from SDFtools.models import blutrac



"""f

users={'hat6974','tes4974'}
locdata = blutrac.getallusers(users)
print locdata
or user in locdata:
    print ""
    print ""
    for item in user:
        print item"""

users={'hat6974'}
blutrac.getallusers(users)
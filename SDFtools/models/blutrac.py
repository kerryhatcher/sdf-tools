__author__ = 'kwhatcher'


from boto.dynamodb2.table import Table
from boto.dynamodb2.layer1 import DynamoDBConnection
import time
from boto.dynamodb import condition
from flask import jsonify

def getuserlast(user):
    conn = DynamoDBConnection()
    results = conn.query(
        'gpstrack',
        key_conditions={'user': {'AttributeValueList': [{'S': user}], 'ComparisonOperator': 'EQ'}},
        scan_index_forward=False,
        limit=1
    )
    #print results
    conn.close()
    return results

def getallusers(users):
    locations = {}
    for user in users:
        userlocation = getuserlast(user)
        #print user
        locations[user] = userlocation['Items']
        print userlocation['Items']
    #print locations[user]
    return locations

def updateuser(user, lat, log):
    item = {
        "epochtime": {
            "N": str(time.time())
        },
        "lat": {
            "N": str(lat)
        },
        "log": {
            "N": str(log)
        },
        "user": {
            "S": user
        }
    }
    conn = DynamoDBConnection()
    results = conn.put_item(
        'gpstrack',
        item
    )
    return results
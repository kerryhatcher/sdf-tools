__author__ = 'kwhatcher'


from boto.dynamodb2.table import Table
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb import condition
from flask import jsonify

def getuserlast(user):
    conn = DynamoDBConnection()
    results = conn.query(
        'gpstrack',
        key_conditions={'user': {'AttributeValueList': [{'S': user}], 'ComparisonOperator': 'EQ'}},
        scan_index_forward=True,
        limit=1
    )
    #print results
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
'''
def getuserlast(user):
    userdata = {}
    gpstracks = Table('gpstrack')
    results = gpstracks.query_2(
        user__eq=user,
        reverse=True,
        limit=1
    )
    for result in results:
        #for item in result:
            #print item
        print jsonify(data=[results for item in result])
        return result._data
'''
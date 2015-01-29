__author__ = 'kwhatcher'
from boto.dynamodb2.fields import HashKey, RangeKey, GlobalAllIndex
from boto.dynamodb2.layer1 import DynamoDBConnection
from boto.dynamodb2.table import Table
from boto.dynamodb2.items import Item


def getallmissions():
    missions = []
    conn = DynamoDBConnection()
    tables = conn.list_tables()
    table = Table('missions', connection=conn)
    results = conn.scan('missions')
    for result in results['Items']:
        print result
    return results['Items']

__author__ = 'kwhatcher'
import yaml
import os
from SDFtools.cache import cache
from flask.ext.stormpath import user


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

def gawxstations():
    filepath = APP_ROOT + "/wxstations.yaml"
    with open(filepath, 'r') as f:
        doc = yaml.load(f)
    return doc["ga"]

@cache.cached(30)
def getsnssubs():
    subscriptions = sns.get_all_subscriptions_by_topic(snstopic_arn)
    return subscriptions





__author__ = 'kwhatcher'
import os
from SDFtools.cache import cache


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@cache.cached(30)
def getsnssubs():
    subscriptions = sns.get_all_subscriptions_by_topic(snstopic_arn)
    return subscriptions





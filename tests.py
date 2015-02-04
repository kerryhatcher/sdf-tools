__author__ = 'kwhatcher'
import SDFtools
from SDFtools.models import missions

def test_get_missions():
    req = missions.getallmissions()
    assert req != ""
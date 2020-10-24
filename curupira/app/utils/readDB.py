from app.models import Localization, WeatherData, WeatherPerEvent
from . import utils
from datetime import datetime, timedelta, timezone
import random
import json

def readMonitoring():

    localizationQuerySet = Localization.objects.values()

    result = list(localizationQuerySet.values())
    
    for i, s in enumerate(result):
        result[i]['lat'] = s['lat']/10000
        result[i]['longit'] = s['longit']/10000
        result[i]['flag'] = random.choice(['positive', 'careful', 'alert'])

    return json.dumps(result)
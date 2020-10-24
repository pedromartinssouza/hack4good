from app.models import Localization, WeatherData, WeatherPerEvent
from . import utils
from datetime import datetime, timedelta, timezone
import random
import json
def readMonitoring():

    localizationQuerySet = Localization.objects.values()

    result = list(localizationQuerySet.values())
    for i, s in enumerate(result):
        parsedLat = s['lat']/10000
        parsedLongit = s['longit']/10000
        historicalData = utils.getHistoricalData(parsedLat, parsedLongit, 5)
        result[i]['lat'] = parsedLat
        result[i]['longit'] = parsedLongit
        result[i]['historical'] = historicalData
        result[i]['flag'] = random.choice(['positive', 'careful', 'alert'])

    return json.dumps(result)
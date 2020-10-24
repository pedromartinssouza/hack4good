from app.models import Localization, WeatherData, WeatherPerEvent
from . import utils
from datetime import datetime, timedelta, timezone

def assignMonitoring(pLat, pLongit, tempUnit):

    localizationQuerySet = Localization.objects.filter(lat = pLat, longit = pLongit)
    localizationQuerySet.update(monitoring = True)

    for days in range(5):
        historicalData = utils.getHistoricalData(pLat, pLongit, days)
        date = datetime.now() - timedelta(days=days)

        weatherDataQuerySet = WeatherData(humidity=historicalData.humidity, 
                                          temperature=historicalData.temperature()['temp'], 
                                          temperatureMetric=tempUnit, 
                                          atmosphericPressure=historicalData.pressure['press'],
                                          wind=historicalData.wind()['speed'], 
                                          localization_id=localizationQuerySet.values('id'),
                                          timeStamp = date
        )
        weatherDataQuerySet.save()

        weatherPerEventQuerySet = WeatherPerEvent(eventId=localizationQuerySet.values('id'), weatherId=weatherDataQuerySet.pk)
        weatherPerEventQuerySet.save()


    return list(localizationQuerySet.values())
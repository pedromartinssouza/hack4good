from app.models import Localization, WeatherData, WeatherPerEvent
from . import utils
from datetime import datetime, timedelta, timezone

def assignMonitoring(pLat, pLongit, pName):

    parsedLat = pLat * 10000
    parsedLongit = pLongit * 10000


    localizationQuerySet = Localization.objects.filter(lat = parsedLat, longit = parsedLongit)

    if(localizationQuerySet.exists()):
        localizationQuerySet.update(monitoring = True, name = pName)
    else:
        createdLocalizationQuerySet = Localization(lat = parsedLat,
                                                   longit = parsedLongit,
                                                   name = pName,
                                                   monitoring = True)
        createdLocalizationQuerySet.save()

    for days in range(5):
        historicalData = utils.getCurrentCompleteWeatherData(parsedLat, parsedLongit)
        date = datetime.now() - timedelta(days=days)
        weatherDataQuerySet = WeatherData(humidity=historicalData['humidity'], 
                                          temperature=historicalData['temperature']['temp'], 
                                          temperatureMetric="Celsius", 
                                          atmosphericPressure=historicalData['pressure']['press'],
                                          wind=historicalData['wind']['speed'], 
                                          localization_id=localizationQuerySet.values('id'),
                                          timeStamp = date
        )
        weatherDataQuerySet.save()

        weatherPerEventQuerySet = WeatherPerEvent(eventId=localizationQuerySet.values('id'), weatherId=weatherDataQuerySet.pk)
        weatherPerEventQuerySet.save()


    return list(localizationQuerySet.values())
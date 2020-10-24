from pyowm.owm import OWM
from pyowm.utils import timestamps
from datetime import datetime, timedelta, timezone

owm = OWM('df60f155083559993c09dbf65eda2992')

mgr = owm.weather_manager()

# what is the epoch for 3 days ago at this time?


def getWeatherData(pLat, pLongit, tempUnit):
    mgr = owm.weather_manager()
    lat = float(pLat)/10000
    longit = float(pLongit)/10000
    observation = mgr.weather_at_coords(lat, longit) 
    weather = observation.weather

    return (weather.temperature(unit=tempUnit), weather.humidity, weather.wind())
    

def getHistoricalData(pLat, pLongit, days):
    date = int((datetime.now() - timedelta(days=days)).replace(tzinfo=timezone.utc).timestamp())

    lat = float(pLat)/10000
    longit = float(pLongit)/10000

    forecastHistory = mgr.one_call_history(lat=lat, lon=longit, dt=date)

    return (forecastHistory.current)
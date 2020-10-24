from pyowm.owm import OWM
from pyowm.utils import timestamps
from datetime import datetime, timedelta, timezone
import json

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

    lat = float(pLat)/10000
    longit = float(pLongit)/10000

    historicalData = list()

    for x in range(5):
        date = int((datetime.now() - timedelta(days=x+1)).replace(tzinfo=timezone.utc).timestamp())
        history = mgr.one_call_history(lat=lat, lon=longit, dt=date)
        historicalData.append({
            'dewpoint': history.current.dewpoint,    
            'temperature': history.current.temperature(unit="celsius"),
            'humidity': history.current.humidity,
            'wind': history.current.wind(unit="meters_sec"),
            'date': date
        })
        

    return (historicalData)

def getCurrentCompleteWeatherData(pLat, pLongit):
    lat = float(pLat)/10000
    longit = float(pLongit)/10000
    date = datetime.now().replace(tzinfo=timezone.utc).timestamp()

    history = mgr.one_call(lat=lat, lon=longit)
    return {
        'dewpoint': history.current.dewpoint,    
        'temperature': history.current.temperature(unit="celsius"),
        'humidity': history.current.humidity,
        'wind': history.current.wind(unit="meters_sec"),
        'date': date,
        'pressure': history.current.pressure
    }

class forecast:  
    def __init__(self, temperature):  
        self.temperature = temperature  